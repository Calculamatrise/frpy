from ..utils.RequestHandler import RequestHandler

class FriendRequest:
	__parent = None
	def __init__(self, data = {}, **kwargs):
		self.__parent = kwargs.get('parent')
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
		if response := RequestHandler.post('/friends/respond_to_friend_request', data = {
			'u_id': self.user.get('id'),
			'action': 'accept'
		}):
			user = response.get('user')
			if self.__parent != None:
				self.__parent.remove(self)
				self.__parent.parent.append(RequestHandler.get('/u/' + user.get('u_name')))

			return True
		return False

	def reject(self):
		if response := RequestHandler.post('/friends/respond_to_friend_request', data = {
			'u_id': self.user.get('id'),
			'action': 'reject'
		}):
			user = response.get('user')
			if self.__parent != None:
				self.__parent.remove(self)
				self.__parent.parent.append(RequestHandler.get('/u/' + user.get('u_name')))

			return True
		return False