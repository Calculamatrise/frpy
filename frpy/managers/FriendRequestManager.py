from ..utils.RequestHandler import RequestHandler

class FriendRequestManager(list):
	def __init__(self, parent):
		self.parent = parent
		self.outgoing = set()

	def accept(self, uid):
		uid = str(uid).lower()
		for request in self:
			if request.user.get('id') == uid or request.user.get('username') == uid:
				return request.accept()

		return False

	def reject(self, uid):
		uid = str(uid).lower()
		for request in self:
			if request.user.get('id') == uid or request.user.get('username') == uid:
				return request.reject()

		return False

	def send(self, username):
		username = username.lower()
		if username in self.outgoing:
			return False

		response = RequestHandler.post('/friends/send_friend_request', data = {
			'u_name': username
		})
		return response and not self.outgoing.add(username)