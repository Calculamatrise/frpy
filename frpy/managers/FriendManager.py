from ..utils.RequestHandler import RequestHandler
from .FriendRequestManager import FriendRequestManager

class FriendManager(list):
	def __init__(self):
		self.requests = FriendRequestManager(self)

	def add(self, username):
		username = username.lower()
		for friend in self:
			if friend.username == username:
				return True

		for request in self.requests:
			if request.user.get('username') == username:
				return request.accept()

		return self.requests.send(username)

	def remove(self, uid):
		for friend in self:
			if friend.get('username') == uid:
				uid = friend.id

		response = RequestHandler.post('/friends/remove_friend', data = {
			'u_id': uid
		})
		return response and response.get('result')