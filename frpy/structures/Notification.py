from ..utils.Events import Events

class Notification:
	def __init__(self, data):
		self.id = self.parseId(data)

	@staticmethod
	def parseId(data):
		if data.get('friend_lb_passed'):
			return Events.get('FriendLeaderboardPassed')
		elif data.get('friend_req_accptd'):
			return Events.get('FriendRequestAccepted')
		elif data.get('friend_req_rcvd'):
			return Events.get('FriendRequestReceived')
		elif data.get('friend_t_challenge'):
			return Events.get('Challenge')
		elif data.get('subscribed_t_publish'):
			return Events.get('SubscribedTrackPublish')
		elif data.get('track_lb_passed'):
			return Events.get('TrackLeaderboardPassed')
		elif data.get('t_uname_mention'):
			return Events.get('TrackUsernameMention')