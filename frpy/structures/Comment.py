class Comment:
	__parent = None
	__track = None
	def __init__(self, parent, track, data):
		self.__parent = parent
		self.__track = track
		comment = data.get('comment') or data
		self.deletable = comment.get('can_delete')
		self.id = comment.get('id')
		self.flagged = comment.get('flagged')
		self.msg = comment.get('msg')
		self.time = comment.get('time')
		if 'user' in data:
			user = data.get('user')
			self.author = {
				'avatar': user.get('img_url_small'),
				'displayName': user.get('d_name'),
				'username': user.get('u_name')
			}

	def delete(self):
		if not deletable:
			self.__parent.client.throw(Exception("Cannot delete a comment which you did not post!"))
			return False

		self.__parent.client.get(f'/track_comments/delete/{self.__track.id}/' + self.id)
		return True

	def reply(self, msg):
		self.__parent.post(f"@{self.author.get('displayName')}, " + str(msg))