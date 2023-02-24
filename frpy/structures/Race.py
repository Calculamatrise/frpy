from ..utils.RequestHandler import RequestHandler
from ..utils.t2t import t2t
from .User import User
from hashlib import sha256
from json import dumps, loads

class Race:
	track = None
	def __init__(self, track, data):
		self.track = track
		race = data.get('race') or data
		self.data = loads(race.get('code'))
		self.desktop = race.get('desktop')
		self.runTicks = race.get('run_ticks')
		self.vehicle = race.get('vehicle')
		if 'place' in data:
			self.placement = data.get('place')

		if 'run_time' in data:
			self.runTime = data.get('run_time')

		if 'tablet' in data:
			self.tablet = data.get('tablet')

		if 'user' in data:
			user = data.get('user')
			self.user = User(user)

	def clone(self):
		uid = RequestHandler.get('/account/settings').get('user').get('id')
		return bool(RequestHandler.post('/track_api/track_run_complete', True, data = {
			't_id': self.track.id,
			'u_id': uid,
			'code': dumps(self.data),
			'fps': 25,
			'run_ticks': self.runTicks,
			'sig': sha256(f'{self.track.id}|{uid}|{dumps(self.data)}|{self.runTicks}|{self.vehicle}|25|erxrHHcksIHHksktt8933XhwlstTekz'.encode('utf-8')).hexdigest(),
			'time': t2t(self.runTicks),
			'vehicle': self.vehicle
		}))

	def remove(self):
		return bool(RequestHandler.post('/moderator/remove_race', True, data = {
			't_id': self.track.id,
			'u_id': self.user.id
		}))