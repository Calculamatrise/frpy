class Builder:
	dict = [chr(x) for x in [*range(48, 58), *range(97, 123)]]
	def __init__(self, importCode = None):
		self.physics = []
		self.scenery = []
		self.powerups = {
			"A": [],
			"O": [],
			"B": [],
			"C": [],
			"G": [],
			"S": [],
			"T": [],
			"W": [],
			"V": [[] for x in list(range(4))]
		}

		if importCode != None:
			importCode = importCode.split('#')
			self.physics.extend([Builder.decode(coord) for coord in line.split(' ')] for line in importCode[0].split(','))
			self.scenery.extend([Builder.decode(coord) for coord in line.split(' ')] for line in importCode[1].split(','))
			for powerup in importCode[2].split(','):
				powerup = powerup.split(' ')
				type = powerup.pop(0)
				if type == 'V':
					self.powerups[type][int(powerup.pop(2)) - 1].append([Builder.decode(coord) for coord in powerup])
					continue

				self.powerups[type].append([Builder.decode(coord) for coord in powerup])

	@staticmethod
	def encode(number):
		result = ""
		negative = number < 0
		number = abs(number)
		while number > 0:
			result = Builder.dict[int(number) % 32] + result
			number = int(number / 32)

		if negative:
			result = "-" + result

		return result.zfill(1);

	@staticmethod
	def decode(string):
		return int(str(string), 32)

	def clear(self):
		self.physics.clear()
		self.scenery.clear()
		for key, powerups in self.powerups:
			if key == 'V':
				for vehicles in powerups:
					vehicles.clear()
				continue

			powerups.clear()

	def strokeDefaultLine(self):
		self.line(-40, 50, 40, 50)

	def strokePhysicsLine(self, x, y, dx, dy):
		self.physics.append([x, y, dx, dy])

	def strokeSceneryLine(self, x, y, dx, dy):
		self.scenery.append([x, y, dx, dy])

	def drawTarget(self, x, y):
		self.powerups['T'].append([x, y])

	def drawSlowmo(self, x, y):
		self.powerups['S'].append([x, y])

	def drawBomb(self, x, y):
		self.powerups['O'].append([x, y])

	def drawCheckpoint(self, x, y):
		self.powerups['C'].append([x, y])

	def drawAntigravity(self, x, y):
		self.powerups['A'].append([x, y])

	def drawBoost(self, x, y):
		self.powerups['B'].append([x, y])

	def drawGravity(self, x, y):
		self.powerups['G'].append([x, y])

	def drawTeleport(self, x, y, dx, dy):
		self.powerups['W'].append([x, y, dx, dy])

	def drawHeli(self, x, y, t):
		self.powerups['V'][1].append([x, y, t])
		return self

	def drawTruck(self, x, y, t):
		self.powerups['V'][2].append([x, y, 2, t])
		return self

	def drawBalloon(self, x, y, t):
		self.powerups['V'][3].append([x, y, 3, t])
		return self

	def drawBlob(self, x, y, t):
		self.powerups['V'][4].append([x, y, 4, t])
		return self

	def export(self):
		return "{physics}#{scenery}#{powerups}".format(
			physics = ",".join([" ".join([Builder.encode(coordinate) for coordinate in line]) for line in self.physics]),
			scenery = ",".join([" ".join([Builder.encode(coordinate) for coordinate in line]) for line in self.scenery]),
			powerups = ",".join([" ".join(powerup) for powerup in sum([sum([[[type] + powerup[:2] + [str(1 + index)] + powerup[2:] for powerup in [[Builder.encode(coord) for coord in powerup] for powerup in powerups]] for index, powerups in enumerate(self.powerups[type])], []) if type == 'V' else [[type] + [Builder.encode(coord) for coord in powerup] for powerup in self.powerups[type]] for type in self.powerups], [])])
		)

	def line(self, x, y, dx, dy, type = 'physics'):
		type = type.lower()
		if type.startswith('b') or type.startswith('p'):
			self.physics.append([x, y, dx, dy])
		elif type.startswith('g') or type.startswith('s'):
			self.scenery.append([x, y, dx, dy])
		else:
			raise TypeError(type + " is not a line type.")

	def powerup(self, x, y, *args):
		args = list(args)
		type = args.pop()
		if not isinstance(self.powerups[type], list):
			raise TypeError(type + " is not a valid powerup type!")

		self.powerups[type].append([x, y, *args])
		return self

	def vehicle(self, x, y, duration, type = 1):
		type = int(type)
		if 1 > type > 4:
			raise TypeError("Vehicle powerup types range between 1 and 4. r:" + str(type))

		self.powerups['V'][type - 1].append([x, y, duration])
		return self