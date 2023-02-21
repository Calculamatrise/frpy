from json import dumps

class Track:
	__client = None
	def __init__(self, parent, data):
		self.__client = parent
		track = data.get('track') or data
		self.author = track.get('author')
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
			self.comments = [data for data in comments]
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

	def toJSON(self):
		client = self.__client
		self.__client = None
		serialized = dumps(self.__dict__, sort_keys=True, indent=4)
		self.__client = client
		return serialized