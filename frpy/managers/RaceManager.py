from .BaseManager import BaseManager
from ..structures.Race import Race
from ..utils.RequestHandler import RequestHandler
from ..utils.t2t import t2t
from hashlib import sha256

class RaceManager(BaseManager):
	__track = None
	def __init__(self, parent):
		self.__track = parent

	def fetch(self, uid, options = {}, **kwargs):
		options = kwargs.get('options') or options or {}
		if not options.get('force') and self.cache.has(uid):
			return self.cache.get(uid)

		res = RequestHandler.post('/track_api/load_races', data = {
			't_id': self.__track.id,
			'u_ids': ','.join(uid) if isinstance(uid, list) else uid
		})
		races = [Race(self.__track, data) for data in res.get('data')]
		for race in races:
			self.cache.set(race.user.id, race)
			if len(races) == 1:
				return race

		return races

	def post(self, code, run_ticks, vehicle = 'MTB'):
		uid = RequestHandler.get('/account/settings').get('user').get('id')
		return bool(RequestHandler.post('/track_api/track_run_complete', True, data = {
			't_id': self.__track.id,
			'u_id': uid,
			'code': code,
			'fps': 25,
			'run_ticks': run_ticks,
			'sig': sha256(f'{self.__track.id}|{uid}|{code}|{run_ticks}|{vehicle}|25|erxrHHcksIHHksktt8933XhwlstTekz'.encode('utf-8')).hexdigest(),
			'time': t2t(run_ticks),
			'vehicle': vehicle
		}))

	def remove(self, uid):
		return bool(RequestHandler.post('/moderator/remove_race', True, data = {
			't_id': self.__track.id,
			'u_id': uid
		}))