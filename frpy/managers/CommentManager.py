from ..structures.Comment import Comment
from ..utils.RequestHandler import RequestHandler

class CommentManager(list):
	__track = None
	__loadMore = True
	def __init__(self, parent):
		self.__track = parent

	def delete(self, cid):
		for comment in self:
			if comment.id == cid:
				return comment.delete()

		return False

	def flag(self, cid):
		for comment in self:
			if comment.id == cid:
				return comment.flag()

		return False

	def loadMore(self, pages = 1):
		pages = int(pages)
		comments = []
		if self.__loadMore == False:
			return comments

		while pages > 0:
			pages -= 1
			last_comment = self[-1]
			response = RequestHandler.post('/track_comments/load_more/' + str(last_comment.id))
			data = response.get('data')
			comments.extend([Comment(self.__track, data) for data in data.get('track_comments')])
			if data.get('track_comments_load_more') != True:
				self.__loadMore = False
				break

		self.extend(comments)
		return comments

	def post(self, msg):
		response = RequestHandler.post('/track_comments/post', data = {
			't_id': self.__track.id,
			'msg': str(msg)
		})