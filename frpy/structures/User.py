from ..managers.FriendManager import FriendManager
from .FriendRequest import FriendRequest
from json import dumps

class User:
	__client = None
	def __init__(self, parent, data, isCurrentUser = False):
		self.__client = parent
		# print(data)
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

	def toJSON(self):
		client = self.__client
		self.__client = None
		serialized = dumps(self.__dict__, sort_keys=True, indent=4)
		self.__client = client
		return serialized