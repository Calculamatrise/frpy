class FriendRequestManager(list):
	__parent = None
	def __init__(self, parent):
		self.__parent = parent
		self.outgoing = set()

	def accept(self, uid):
		if isinstance(uid, str):
			for request in self:
				if request.user.get('username') == uid.lower():
					uid = request.user.get('id')

		response = self.__parent.client.post('/friends/respond_to_friend_request', data = {
			'u_id': uid,
			'action': 'accept'
		})
		if 'user' in response:
			user = response.get('user')
			for request in self:
				if request.user.get('id') == user.get('u_id'):
					self.remove(request)
					self.__parent.append(request.user)

			return True
		return False

	def reject(self, uid):
		if isinstance(uid, str):
			for request in self:
				if request.user.get('username') == uid.lower():
					uid = request.user.get('id')

		response = self.__parent.client.post('/friends/respond_to_friend_request', data = {
			'u_id': uid,
			'action': 'reject'
		})
		if 'user' in response:
			user = response.get('user')
			for request in self:
				if request.user.get('id') == user.get('u_id'):
					self.remove(request)

			return True
		return False

	def send(self, username):
		username = username.lower()
		if username in self.outgoing:
			return False

		response = self.__parent.client.post('/friends/send_friend_request', data = {
			'u_name': username
		})
		return response and not self.outgoing.add(username)