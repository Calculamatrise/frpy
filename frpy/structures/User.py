from ..managers.CosmeticManager import CosmeticManager
from ..managers.FriendManager import FriendManager
from ..utils.RequestHandler import RequestHandler
from .FriendRequest import FriendRequest

class User:
	def __init__(self, data = {}, isCurrentUser = False):
		user = data.get('user') or data
		self.admin = user.get('admin')
		self.avatar = user.get('img_url_large') or user.get('img_url_medium') or user.get('img_url_small')
		self.classic = user.get('classic')
		self.cosmetics = CosmeticManager(self, user.get('cosmetics'))
		self.displayName = user.get('d_name')
		self.forums = user.get('forum_url')
		self.id = user.get('u_id')
		self.moderator = user.get('moderator')
		self.plus = user.get('plus')
		self.username = user.get('u_name')
		if 'activity_time_ago' in data:
			self.lastPlayed = data.get('activity_time_ago')
			# or fetch a friend and compute lastPlayed

		if 'a_ts' in data:
			self.lastPlayedTimestamp = data.get('a_ts')

		if 'created_tracks' in data:
			createdTracks = data.get('created_tracks')
			self.createdTracks = createdTracks.get('tracks')

		self.friends = FriendManager()
		if 'friends' in data:
			friends = data.get('friends')
			self.friends.extend([User(friend) for friend in friends.get('friends_data')])

		if 'friend_requests' in data:
			friendRequests = data.get('friend_requests')
			self.friends.requests.extend([FriendRequest(data, parent = self.friends.requests) for data in friendRequests.get('request_data')])

		if 'has_max_friends' in data:
			self.friendLimitReached = data.get('has_max_friends')
		
		if 'liked_tracks' in data:
			likedTracks = data.get('liked_tracks')
			self.likedTracks = likedTracks.get('tracks')

		if 'recently_ghosted_tracks' in data:
			recentlyCompleted = data.get('recently_ghosted_tracks')
			self.recentlyCompleted = recentlyCompleted.get('tracks')

		if 'recently_played_tracks' in data:
			recentlyPlayed = data.get('recently_played_tracks')
			self.recentlyPlayed = recentlyPlayed.get('tracks') # map as Track structures

		if 'subscribe' in data:
			subscribe = data.get('subscribe')
			if subscribe:
				self.subscriberCount = subscribe.get('count')

		if 'user_info' in data:
			info = data.get('user_info')
			if isinstance(info, dict):
				self.bio = info.get('about')

		if 'user_mobile_stats' in data:
			stats = data.get('user_mobile_stats')
			if stats.get('connected'):
				self.mobileStats = {
					'level': stats.get('lvl'),
					'wins': stats.get('wins'),
					'headCount': stats.get('headCount'),
					'connected': stats.get('connected')
				}

		if 'user_stats' in data:
			stats = data.get('user_stats')
			self.stats = {
				'totalPoints': stats.get('tot_pts'),
				'completed': stats.get('cmpltd'),
				'rated': stats.get('rtd'),
				'comments': stats.get('cmmnts'),
				'created': stats.get('crtd'),
				'headCount': stats.get('head_cnt'),
				'totalHeadCount': stats.get('total_head_cnt')
			}

	def subscribe(self):
		return bool(RequestHandler.post('/track_api/subscribe', True, data = {
			'sub_uid': self.id,
			'subscribe': 1
		}))

	def unsubscribe(self):
		return bool(RequestHandler.post('/track_api/subscribe', True, data = {
			'sub_uid': self.id,
			'subscribe': 0
		}))

	def updatePersonalData(self, name, value):
		return bool(RequestHandler.post('/account/update_personal_data', True, data = {
			'name': name,
			'value': value
		}))

	def deletePersonalData(self, name, value):
		return bool(RequestHandler.post('/account/delete_all_personal_data', True))

	def selectProfileImage(self, img_type):
		return bool(RequestHandler.post('/account/update_photo', True, data = {
			'img_type': img_type
		}))

	def changeDescription(self, description):
		return bool(RequestHandler.post('/account/edit_profile', True, data = {
			'name': 'about',
			'value': description
		}))

	def changePassword(self, old_password, new_password):
		return bool(RequestHandler.post('/account/change_password', True, data = {
			'old_password': old_password,
			'new_password': new_password
		}))

	def changeUsername(self, username):
		if self.id == RequestHandler.get('/account/settings').get('user').get('id'):
			return bool(RequestHandler.post('/account/edit_profile', True, data = {
				'name': 'u_name',
				'value': username
			}))

		return bool(RequestHandler.post('/moderator/change_username', True, data = {
			'u_id': self.id,
			'username': username
		}))

	def changeUsernameAsAdmin(self, username):
		return bool(RequestHandler.post('/admin/change_username', True, data = {
			'change_username_current': self.username,
			'change_username_new': username
		}))

	def setForumPassword(self, password):
		return bool(RequestHandler.post('/account/update_forum_account', True, data = {
			'password': password
		}))

	def transferCoins(self, amount, message = ''):
		return bool(RequestHandler.post('/account/plus_transfer_coins', True, data = {
			'transfer_coins_to': self.username,
			'transfer_coins_amount': amount,
			'msg': message
		}))

	def ban(self):
		return bool(RequestHandler.post('/moderator/ban_user', True, data = {
			'u_id': self.id
		}))

	def banAsAdmin(self, duration = 0, delete_races = False):
		return bool(RequestHandler.post('/admin/ban_user', True, data = {
			'ban_secs': int(duration),
			'delete_race_stats': delete_races,
			'username': self.username
		}))

	def unban(self):
		return bool(RequestHandler.post('/moderator/unban_user', True, data = {
			'u_id': self.id
		}))

	def changeEmail(self, email):
		return bool(RequestHandler.post('/moderator/change_email', True, data = {
			'u_id': self.id,
			'email': email
		}))

	def changeEmailAsAdmin(self, email):
		return bool(RequestHandler.post('/admin/change_user_email', True, data = {
			'username': self.username,
			'email': email
		}))

	def deactivate(self):
		return bool(RequestHandler.post('/admin/deactivate_user', True, data = {
			'username': self.username
		}))

	def delete(self):
		return bool(RequestHandler.post('/admin/delete_user_account', True, data = {
			'username': self.username
		}))

	def toggleOA(self):
		return bool(RequestHandler.post('/moderator/toggle_official_author/' + str(self.id), True))

	def toggleClassicAuthorAsAdmin(self):
		return bool(RequestHandler.post('/admin/toggle_classic_user', True, data = {
			'toggle_classic_uname': self.username
		}))

	def addPlusDays(self, days, remove):
		return bool(RequestHandler.post('/admin/add_plus_days', True, data = {
			'add_plus_days': days,
			'username': self.username,
			'add_plus_remove': remove
		}))

	def addWonCoins(self, coins):
		return bool(RequestHandler.post('/admin/add_won_coins', True, data = {
			'coins_username': self.username,
			'num_coins': int(coins)
		}))

	def messagingBan(self):
		return bool(RequestHandler.post('/admin/user_ban_messaging', True, data = {
			'messaging_ban_username': self.username
		}))

	def uploadingBan(self):
		return bool(RequestHandler.post('/admin/user_ban_uploading', True, data = {
			'uploading_ban_username': self.username
		}))