from .BaseManager import BaseManager
from ..structures.Track import Track
from ..utils.RequestHandler import RequestHandler

class TrackManager(BaseManager):
	def fetch(self, id, options = {}, **kwargs):
		id = str(id)
		options = kwargs.get('options') or options or {}
		if not options.get('force') and self.cache.has(id):
			return self.cache.get(id)

		entry = RequestHandler.get('/t/' + id)
		if entry:
			entry = Track(entry)
			self.cache.set(id.lower(), entry)

		return entry

	def lookup(self, query):
		response = RequestHandler.post('/search/t/' + query)
		if response:
			# maybe cache these results
			return [Track(entry) for entry in response.get('tracks')]

		return []

	def flag(self, tid):
		return bool(RequestHandler.get('/track_api/flag/' + str(tid), True))

	def addToDaily(self, tid, lives = 30, refill_cost = 10, gems = 500):
		return RequestHandler.post('/moderator/add_track_of_the_day', True, data = {
			't_id': tid,
			'lives': lives,
			'rfll_cst': refill_cost,
			'gems': gems
		})

	def removeFromDaily(self, tid):
		return RequestHandler.post('/admin/removeTrackOfTheDay', True, data = {
			't_id': self.id,
			'd_ts': None
		})

	def feature(self, tid):
		return RequestHandler.post(f'/track_api/feature_track/{str(tid)}/1', True)

	def unfeature(self, tid):
		return RequestHandler.post(f'/track_api/feature_track/{str(tid)}/0', True)

	def hide(self, tid):
		return RequestHandler.post('/moderator/hide_track/' + str(tid), True)

	def unhide(self, tid):
		return RequestHandler.post('/moderator/unhide_track/' + str(tid), True)

	def hideAsAdmin(self, tid):
		return RequestHandler.post('/admin/hide_track', True, data = {
			'track_id': tid
		})