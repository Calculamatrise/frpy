class Race:
	__client = None
	def __init__(self, client, data):
		self.__client = client
		race = data.get('race') or data
		self.data = race.get('code')
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
			self.user = {
				'avatar': user.get('img_url_small'),
				'cosmetics': user.get('cosmetics'),
				'displayName': user.get('d_name'),
				'id': user.get('id'),
				'username': user.get('u_name')
			}