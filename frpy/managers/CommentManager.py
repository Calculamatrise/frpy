from ..structures.Comment import Comment

class CommentManager(list):
	__track = None
	__loadMore = True
	def __init__(self, parent, client):
		self.client = client
		self.__track = parent

	def loadMore(self, pages = 1):
		pages = int(pages)
		comments = []
		if self.__loadMore == False:
			return comments

		while pages > 0:
			pages -= 1
			last_comment = str(self.__track.id)
			response = self.client.post('/track_comments/load_more/' + str(self.__track.id))
			data = response.get('data')
			comments.extend([Comment(self, self.__track, data) for data in data.get('track_comments')])
			if data.get('track_comments_load_more') != True:
				self.__loadMore = False
				break

		self.extend(comments)
		return comments

	def post(self, msg):
		response = self.client.post('/track_comments/post', data = {
			't_id': self.__track.id,
			'msg': msg
		})