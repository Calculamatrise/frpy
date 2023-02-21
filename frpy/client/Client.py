from .BaseClient import BaseClient
from ..managers.CosmeticManager import CosmeticManager
from ..managers.TrackManager import TrackManager
from ..managers.UserManager import UserManager

class Client(BaseClient):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cosmetics = CosmeticManager(self)
		self.tracks = TrackManager(self)
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

	def equipHead(self, item_id):
		return self.post('/store/equip/', data = {
			item_id
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

	def redeemCoupon(self):
		return self.post('/store/redeemCouponCode/')

	def transferCoins(self, user, amount, message = ''):
		return bool(self.post('/account/plus_transfer_coins', data = {
			'transfer_coins_to': user,
			'transfer_coins_amount': amount,
			'msg': message
		}))