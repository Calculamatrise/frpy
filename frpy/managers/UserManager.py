from .BaseManager import BaseManager
from ..structures.User import User
from ..utils.RequestHandler import RequestHandler

class UserManager(BaseManager):
	def fetch(self, uid, options = {}, **kwargs):
		options = kwargs.get('options') or options or {}
		if not options.get('force') and self.cache.has(uid):
			return self.cache.get(uid)

		entry = RequestHandler.get('/u/' + uid)
		if entry:
			entry = User(entry)
			self.cache.set(uid.lower(), entry)

		return entry

	def lookup(self, query):
		response = RequestHandler.post('/search/u_mention_lookup/' + query)
		if response:
			return [User(entry) for entry in response.get('data')]

		return []

	def ban(self, uid):
		return bool(RequestHandler.post('/moderator/ban_user', True, data = {
			'u_id': uid
		}))

	def ban(self, username, duration = 0, delete_races = False):
		return bool(RequestHandler.post('/moderator/ban_user', True, data = {
			'ban_secs': int(duration),
			'delete_race_stats': delete_races,
			'username': username
		}))

	def unban(self, uid):
		return bool(RequestHandler.post('/moderator/unban_user', True, data = {
			'u_id': uid
		}))

	def deactivate(self, username):
		return bool(RequestHandler.post('/admin/deactivate_user', True, data = {
			'username': username
		}))

	def delete(self, username):
		return bool(RequestHandler.post('/admin/delete_user_account', True, data = {
			'username': username
		}))

	def toggleOA(self, uid):
		return bool(RequestHandler.post('/moderator/toggle_official_author/' + str(uid), True))

	def toggleClassicAuthorAsAdmin(self, username):
		return bool(RequestHandler.post('/admin/toggle_classic_user', True, data = {
			'toggle_classic_uname': username
		}))

	def addPlusDays(self, username, days, remove):
		return bool(RequestHandler.post('/admin/add_plus_days', True, data = {
			'add_plus_days': days,
			'username': username,
			'add_plus_remove': remove
		}))

	def addWonCoins(self, username, coins):
		return bool(RequestHandler.post('/admin/add_won_coins', True, data = {
			'coins_username': username,
			'num_coins': int(coins)
		}))

	def messagingBan(self, username):
		return bool(RequestHandler.post('/admin/user_ban_messaging', True, data = {
			'messaging_ban_username': username
		}))

	def uploadingBan(self, username):
		return bool(RequestHandler.post('/admin/user_ban_uploading', True, data = {
			'uploading_ban_username': username
		}))