from ..managers.FriendManager import FriendManager
from .FriendRequest import FriendRequest
from json import dumps

class User:
	__client = None
	def __init__(self, parent, data = {}, isCurrentUser = False):
		self.__client = parent
		user = data.get('user') or data
		self.admin = user.get('admin')
		self.avatar = user.get('img_url_large') or user.get('img_url_medium') or user.get('img_url_small')
		self.classic = user.get('classic')
		self.cosmetics = user.get('cosmetics')
		self.displayName = user.get('d_name')
		self.forums = user.get('forum_url')
		self.id = user.get('u_id')
		self.moderator = user.get('moderator') or False
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

		self.friends = FriendManager(self.__client)
		if 'friends' in data:
			friends = data.get('friends')
			self.friends.count = friends.get('friend_cnt')
			self.friends.extend([User(self.__client, friend) for friend in friends.get('friends_data')])

		if 'friend_requests' in data:
			friendRequests = data.get('friend_requests')
			self.friends.requests.extend([FriendRequest(self.friends.requests, data) for data in friendRequests.get('request_data')])

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
		return bool(self.__client.post('/track_api/subscribe', data = {
			'sub_uid': self.id,
			'subscribe': 1
		}))

	def unsubscribe(self):
		return bool(self.__client.post('/track_api/subscribe', data = {
			'sub_uid': self.id,
			'subscribe': 0
		}))

	def updatePersonalData(self, name, value):
		return bool(self.__client.post('/account/update_personal_data', data = {
			'name': name,
			'value': value
		}))

	def deletePersonalData(self, name, value):
		return bool(self.__client.post('/account/delete_all_personal_data'))

	def selectProfileImage(self, img_type):
		return bool(self.__client.post('/account/update_photo', data = {
			'img_type': img_type
		}))

	def changeDescription(self, description):
		return bool(self.__client.post('/account/edit_profile', data = {
			'name': 'about',
			'value': description
		}))

	def changePassword(self, old_password, new_password):
		return bool(self.__client.post('/account/change_password', data = {
			'old_password': old_password,
			'new_password': new_password
		}))

	def changeUsername(self, username):
		if self.id == self.__client.user.id:
			return bool(self.__client.post('/account/edit_profile', data = {
				'name': 'u_name',
				'value': username
			}))

		return bool(self.__client.post('/moderator/change_username', data = {
			'u_id': self.id,
			'username': username
		}))

	def changeUsernameAsAdmin(self, username):
		return bool(self.__client.post('/admin/change_username', data = {
			'change_username_current': self.username,
			'change_username_new': username
		}))

	def setForumPassword(self, password):
		return bool(self.__client.post('/account/update_forum_account', data = {
			'password': password
		}))

	def transferCoins(self, amount, message = ''):
		return bool(self.__client.post('/account/plus_transfer_coins', data = {
			'transfer_coins_to': self.username,
			'transfer_coins_amount': amount,
			'msg': message
		}))

	def ban(self):
		return bool(self.__client.post('/moderator/ban_user', data = {
			'u_id': self.id
		}))

	def banAsAdmin(self, duration = 0, delete_races = False):
		return bool(self.__client.post('/admin/ban_user', data = {
			'ban_secs': int(duration),
			'delete_race_stats': delete_races,
			'username': self.username
		}))

	def unban(self):
		return bool(self.__client.post('/moderator/unban_user', data = {
			'u_id': self.id
		}))

	def changeEmail(self, email):
		return bool(self.__client.post('/moderator/change_email', data = {
			'u_id': self.id,
			'email': email
		}))

	def changeEmailAsAdmin(self, email):
		return bool(self.__client.post('/admin/change_user_email', data = {
			'username': self.username,
			'email': email
		}))

	def deactivate():
		return bool(self.__client.post('/admin/deactivate_user', data = {
			'username': self.username
		}))

	def delete():
		return bool(self.__client.post('/admin/delete_user_account', data = {
			'username': self.username
		}))

	def toggleOA():
		return bool(self.__client.post('/moderator/toggle_official_author/' + str(self.id)))

	def toggleClassicAuthorAsAdmin():
		return bool(self.__client.post('/admin/toggle_classic_user', data = {
			'toggle_classic_uname': self.username
		}))

	def addPlusDays(self, days, remove):
		return bool(self.__client.post('/admin/add_plus_days', data = {
			'add_plus_days': days,
			'username': self.username,
			'add_plus_remove': remove
		}))

	def addWonCoins(self, coins):
		return bool(self.__client.post('/admin/add_won_coins', data = {
			'coins_username': self.username,
			'num_coins': int(coins)
		}))

	def messagingBan(self):
		return bool(self.__client.post('/admin/user_ban_messaging', data = {
			'messaging_ban_username': self.username
		}))

	def uploadingBan(self):
		return bool(self.__client.post('/admin/user_ban_uploading', data = {
			'uploading_ban_username': self.username
		}))

	def toJSON(self):
		clone = self.__dict__
		del clone[f'_{self.__class__.__name__}__client']
		return dumps(clone, sort_keys=True, indent=4)