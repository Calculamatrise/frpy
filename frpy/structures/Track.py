from ..managers.CommentManager import CommentManager
from .Comment import Comment
from .Race import Race
from .User import User
from json import dumps

class Track:
	__client = None
	__leaderboard = []
	def __init__(self, parent, data):
		self.__client = parent
		track = data.get('track') or data
		self.author = User(self.__client)
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

		self.comments = CommentManager(self, self.__client)
		if 'track_comments' in data:
			comments = data.get('track_comments')
			self.comments.extend([Comment(self.comments, self, data) for data in comments])
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
		return self.__client.post('/challenge/send', data = {
			'msg': str(message),
			'track_slug': self.id,
			'users': ','.join(users)
		}).get('debug')

	def flag(self):
		self.__client.get('/track_api/flag/' + str(self.id))
		return True

	def leaderboard(self):
		res = self.__client.post('/track_api/load_leaderboard', data = {
			't_id': self.id
		})
		self.__leaderboard = [Race(self.__client, data) for data in res.get('track_leaderboard')]
		return self.__leaderboard

	def loadRaces(self, users):
		return self.__client.post('/track_api/load_races', data = {
			't_id': self.id,
			'u_ids': ','.join(users)
		})

	def vote(self, vote):
		vote = int(vote)
		return self.__client.post('/track_api/vote', data = {
			't_id': self.id,
			'vote': vote
		})

	def addToDaily(self, lives = 30, refill_cost = 10, gems = 500):
		return self.__client.post('/moderator/add_track_of_the_day', data = {
			't_id': self.id,
			'lives': lives,
			'rfll_cst': refill_cost,
			'gems': gems
		})

	def removeFromDaily(self):
		return self.__client.post('/admin/removeTrackOfTheDay', data = {
			't_id': self.id,
			'd_ts': None
		})

	def feature(self):
		self.__client.post(f'/track_api/feature_track/{str(self.id)}/1')
		self.featured = True
		return self.featured

	def unfeature(self):
		self.__client.post(f'/track_api/feature_track/{str(self.id)}/0')
		self.featured = False
		return self.featured

	def hide(self):
		self.__client.post('/moderator/hide_track/' + str(self.id))
		self.hidden = True
		return self.hidden

	def unhide(self):
		self.__client.post('/moderator/unhide_track/' + str(self.id))
		self.hidden = False
		return self.hidden

	def hideAsAdmin(self):
		return self.__client.post('/admin/hide_track', data = {
			'track_id': self.id
		})

	def toJSON(self):
		clone = self.__dict__
		del clone[f'_{self.__class__.__name__}__client']
		return dumps(clone, sort_keys=True, indent=4)