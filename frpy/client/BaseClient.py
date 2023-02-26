from ..utils.EventEmitter import EventEmitter
from ..utils.Events import Events
from ..utils.RequestHandler import RequestHandler
from ..structures.Cosmetic import Cosmetic
from ..structures.Notification import Notification
from ..structures.User import User
import requests
import time

class BaseClient(EventEmitter):
	__interval = 1e3;
	__token = None
	def __init__(self, **kwargs):
		self.user = None
		if kwargs.get('listen'):
			self.__interval = int(kwargs.get('interval'))
			self.once('ready', self.__requestDatapoll)

	def __requestDatapoll(self, *args):
		response = self.datapoll()
		response['notification_count'] = 1
		if response.get('notification_count') > 0:
			notifications = self.notifications()
			self.emit('raw', notifications)
			notificationDays = notifications.get('notification_days')
			notifications = [Notification(data) for data in notificationDays[0].get('notifications')[:response.get('notification_count')]]
			for notification in notifications:
				self.emit(notification.id, notification)

		time.sleep(self.__interval / 1e3)
		self.__requestDatapoll()

	def throw(self, exception):
		if self.listeners('error') > 0:
			self.emit('error', exception)
		else:
			raise exception

	def login(self, token):
		if isinstance(token, dict):
			self.__token = 'True'
			response = RequestHandler.post('/auth/standard_login', data = token)
			if 'app_signed_request' in response:
				token = response.get('app_signed_request')

		response = RequestHandler.assertToken(token)
		if not response:
			return

		self.user = User(RequestHandler.get('/u/' + response.get('d_name')), True)
		self.user.moderator = response.get('moderator')
		for index, partial in enumerate(self.user.friends):
			self.user.friends[index] = self.users.fetch(partial.username)

		for head in [Cosmetic(data) for data in RequestHandler.get('/store/gear').get('gear').get('head_gear')]:
			self.user.cosmetics.cache.set(head.id, head)

		self.emit(Events.get('ClientReady'))
		return self

	def logout(self):
		RequestHandler.deleteToken()
		self.emit('disconnected')

	def datapoll(self):
		return RequestHandler.post('/datapoll/poll_request', True, data = {
			'notifications': 'true'
		})

	def notifications(self):
		return RequestHandler.get('/notifications', True)