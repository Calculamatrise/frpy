from .BaseManager import BaseManager
from ..structures.User import User

class UserManager(BaseManager):
	def fetch(self, uid, options = {}, **kwargs):
		options = kwargs.get('options') or options or {}
		if not options.get('force') and self.cache.has(uid):
			return self.cache.get(uid)

		entry = self.client.get('/u/' + uid)
		if entry:
			entry = User(self.client, entry)
			self.cache.set(uid.lower(), entry)

		return entry

	def lookup(self, query):
		response = self.client.post('/search/u_mention_lookup/' + query)
		if response:
			return [User(entry) for entry in response.get('data')]

		return []