from .BaseClient import BaseClient
from ..managers.UserManager import UserManager

class Client(BaseClient):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.users = UserManager(self)

	def changeName(self, username):
		return self.post(f'/account/edit_profile/', data = {
			'name': 'u_name',
			'value': username
		})

	def changeDesc(self, description):
		return self.post('/account/edit_profile/', data = {
			'name': 'about',
			'value': description
		})

	def changePassword(self, old_password, new_password):
		return self.post('/account/change_password/', data = {
			old_password,
			new_password
		})

	def changeForumsPassword(self, password):
		return self.post('/account/update_forum_account/', data = {
			password
		})

	def buyHead(self):
		return self.post('/store/buy/')

	def equipHead(self, item_id):
		return self.post('/store/equip/', data = {
			item_id
		})

	def addFriend(self, u_name):
		return self.post('/friends/send_friend_request/?u_name={f}', data = {
			u_name
		})

	def removeFriend(self, u_id):
		return self.post('/friends/remove_friend/', data = {
			u_id
		})

	def acceptFriendRequest(self, username):
		return self.post('/friends/respond_to_friend_request/', data = {
			'u_name': username,
			'action': 'accept'
		})

	def rejectFriendRequest(self, username):
		return self.post('/friends/respond_to_friend_request/', data = {
			'u_name': username,
			'action': 'reject'
		})

	def challenge(self, users, m, track):
		return self.post('/challenge/send/', data = {
			'users': ','.join(users)
		})

	def comment(self):
		return self.post('/track_comments/post/')

	def vote(self, t_id, vote):
		return self.post('/track_api/vote/', data = {
			t_id,
			vote
		})

	def subscribe(self):
		return self.post('/track_api/subscribe/')

	def redeemCoupon(self):
		return self.post('/store/redeemCouponCode/')

	def publish(self):
		return self.post('/create/submit/', data = {})