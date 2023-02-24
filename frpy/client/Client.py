from .BaseClient import BaseClient
from ..managers.TrackManager import TrackManager
from ..managers.UserManager import UserManager
from ..utils.RequestHandler import RequestHandler

class Client(BaseClient):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.tracks = TrackManager(self)
		self.users = UserManager(self)

	def changeName(self, username):
		return RequestHandler.post(f'/account/edit_profile/', data = {
			'name': 'u_name',
			'value': username
		})

	def changeDesc(self, description):
		return RequestHandler.post('/account/edit_profile/', data = {
			'name': 'about',
			'value': description
		})

	def changePassword(self, old_password, new_password):
		return RequestHandler.post('/account/change_password/', data = {
			old_password,
			new_password
		})

	def changeForumsPassword(self, password):
		return RequestHandler.post('/account/update_forum_account/', data = {
			password
		})

	def equipHead(self, item_id):
		return RequestHandler.post('/store/equip/', data = {
			item_id
		})

	def challenge(self, users, m, track):
		return RequestHandler.post('/challenge/send/', data = {
			'users': ','.join(users)
		})

	def comment(self):
		return RequestHandler.post('/track_comments/post/')

	def vote(self, t_id, vote):
		return RequestHandler.post('/track_api/vote/', data = {
			t_id,
			vote
		})

	def redeemCoupon(self):
		return RequestHandler.post('/store/redeemCouponCode/')

	def transferCoins(self, user, amount, message = ''):
		return bool(RequestHandler.post('/account/plus_transfer_coins', data = {
			'transfer_coins_to': user,
			'transfer_coins_amount': amount,
			'msg': message
		}))