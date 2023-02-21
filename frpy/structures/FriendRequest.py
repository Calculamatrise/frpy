class FriendRequest:
	__parent = None
	def __init__(self, parent, data):
		self.__parent = parent
		self.timeAgo = data['request'].get('time_ago')
		if 'user' in data:
			user = data.get('user')
			self.user = {
				'avatar': user.get('img_url_small'),
				'displayName': user.get('d_name'),
				'id': user.get('u_id'),
				'username': user.get('u_name')
			}

	def accept(self):
		return self.__parent.accept(self.user.get('username'))

	def reject(self):
		return self.__parent.reject(self.user.get('username'))