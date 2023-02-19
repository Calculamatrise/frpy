from ..utils.EventEmitter import EventEmitter
from ..utils.Events import Events
from ..utils.helpers import getUser
from ..structures.Notification import Notification
import requests
import time
from threading import Thread

class BaseClient(EventEmitter):
	__interval = 1e3;
	__token = None
	def __init__(self, **kwargs):
		self.user = None
		if kwargs.get('listen'):
			self.__interval = int(kwargs.get('interval'))
			self.once('ready', self.__requestDatapoll)

	def __request(self, endpoint, *args, **kwargs):
		if not self.__token:
			self.throw(Exception("Client is not logged in!"))

		args = [f'https://www.freeriderhd.com{endpoint}?ajax=true&t_1=ref&t_2=desk&app_signed_request=' + self.__token, *args]
		try:
			if args.pop().lower().startswith('p'):
				return requests.post(*args, **kwargs).json()

			return requests.get(*args, **kwargs).json()
		except Exception as e:
			self.throw(e)

	def __requestDatapoll(self, *args):
		response = self.datapoll()
		self.emit('raw', response)
		if response.get('notification_count') > 0:
			notifications = self.notifications()
			notificationDays = notifications.get('notification_days')
			notifications = notificationDays[0].get('notifications')[:response.get('notification_count')]
			for notification in notifications:
				self.emit('notification', Notification(notification))

		time.sleep(self.__interval / 1e3)
		self.__requestDatapoll()

	def __verifyToken(self, token):
		try:
			self.__token = token
			response = self.get('/account/settings')
			if 'user' not in response:
				raise Exception("Invalid token!")

			return response.get('user')
		except Exception as e:
			self.__token = None
			self.throw(e)

	def throw(self, exception):
		if self.listeners('error') > 0:
			self.emit('error', exception)
		else:
			raise exception

	def get(self, *args):
		return self.__request(*args, 'get')

	def post(self, *args, **kwargs):
		return self.__request(*args, 'post', **kwargs)

	def login(self, token):
		if isinstance(token, dict):
			self.__token = 'True'
			response = self.post('/auth/standard_login', data = token)
			if 'app_signed_request' in response:
				token = response.get('app_signed_request')

		response = self.__verifyToken(token)
		if not response:
			return

		self.user = getUser(response.get('d_name'))
		self.user['moderator'] = response.get('moderator')
		self.emit('ready')
		return self

	def logout(self):
		self.token = None

	def datapoll(self):
		return self.post('/datapoll/poll_request', data = {
			'notifications': 'true'
		})

	def notifications(self):
		return self.get('/notifications')