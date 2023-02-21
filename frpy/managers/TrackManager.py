from .BaseManager import BaseManager
from ..structures.Track import Track

class TrackManager(BaseManager):
	def fetch(self, id, options = {}, **kwargs):
		id = str(id)
		options = kwargs.get('options') or options or {}
		if not options.get('force') and self.cache.has(id):
			return self.cache.get(id)

		entry = self.client.get('/t/' + id)
		if entry:
			entry = Track(self.client, entry)
			self.cache.set(id.lower(), entry)

		return entry

	def lookup(self, query):
		response = self.client.post('/search/t/' + query)
		if response:
			return [Track(entry) for entry in response.get('tracks')]

		return []