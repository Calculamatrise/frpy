from ..managers.CommentManager import CommentManager
from ..managers.RaceManager import RaceManager
from ..utils.RequestHandler import RequestHandler
from .Comment import Comment
from .Race import Race
from .User import User

class Track:
	__leaderboard = []
	def __init__(self, data = {}):
		self.comments = CommentManager(self)
		self.races = RaceManager(self)
		track = data.get('track') or data
		self.author = User()
		self.author.avatar = track.get('author_img_small')
		self.author.displayName = track.get('author')
		self.author.id = track.get('u_id')
		self.author.username = track.get('author_slug')
		self.createdAt = track.get('date')
		self.createdDateAgo = track.get('date_ago')
		self.description = track.get('descr')
		self.featured = track.get('featured')
		self.hidden = track.get('hide')
		self.id = track.get('id')
		self.size = track.get('kb_size')
		self.thumbnail = track.get('img_768x250') or track.get('img')
		self.title = track.get('title')
		self.vehicle = track.get('vehicle')
		self.vehicles = track.get('vehicles')
		if 'totd' in data:
			totd = data.get('totd')
			self.trackOfTheDay = {
				'entries': totd.get('entries'),
				'gems': totd.get('gems'),
				'lives': totd.get('lives'),
				'refillCost': totd.get('refill_cost')
			}

		if 'track_comments' in data:
			comments = data.get('track_comments')
			self.comments.extend([Comment(self, data) for data in comments])
			self.maxCommentLength = data.get('max_comment_length') or 500

		if 'track_stats' in data:
			stats = data.get('track_stats')
			self.stats = {
				'averageRating': stats.get('vote_percent'),
				'averageTime': stats.get('avg_time'),
				'completionRate': stats.get('cmpltn_rate'),
				'downVotes': stats.get('dwn_votes'),
				'firstRuns': stats.get('first_runs'),
				'plays': stats.get('plays'),
				'runs': stats.get('runs'),
				'upVotes': stats.get('up_votes'),
				'votes': stats.get('votes')
			}

	def challenge(self, users = [], message = ''):
		return RequestHandler.post('/challenge/send', True, data = {
			'msg': str(message),
			'track_slug': self.id,
			'users': ','.join(users)
		}).get('debug')

	def flag(self):
		return bool(RequestHandler.get('/track_api/flag/' + str(self.id), True))

	def leaderboard(self):
		res = RequestHandler.post('/track_api/load_leaderboard', data = {
			't_id': self.id
		})
		self.__leaderboard = [Race(data) for data in res.get('track_leaderboard')]
		return self.__leaderboard

	def vote(self, vote):
		vote = int(vote)
		return RequestHandler.post('/track_api/vote', True, data = {
			't_id': self.id,
			'vote': vote
		})

	def addToDaily(self, lives = 30, refill_cost = 10, gems = 500):
		return RequestHandler.post('/moderator/add_track_of_the_day', True, data = {
			't_id': self.id,
			'lives': lives,
			'rfll_cst': refill_cost,
			'gems': gems
		})

	def removeFromDaily(self):
		return RequestHandler.post('/admin/removeTrackOfTheDay', True, data = {
			't_id': self.id,
			'd_ts': None
		})

	def feature(self):
		RequestHandler.post(f'/track_api/feature_track/{str(self.id)}/1', True)
		self.featured = True
		return True

	def unfeature(self):
		RequestHandler.post(f'/track_api/feature_track/{str(self.id)}/0', True)
		self.featured = False
		return True

	def hide(self):
		RequestHandler.post('/moderator/hide_track/' + str(self.id), True)
		self.hidden = True
		return True

	def unhide(self):
		RequestHandler.post('/moderator/unhide_track/' + str(self.id), True)
		self.hidden = False
		return True

	def hideAsAdmin(self):
		return RequestHandler.post('/admin/hide_track', True, data = {
			'track_id': self.id
		})