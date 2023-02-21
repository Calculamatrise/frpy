class Map(dict):
	def has(self, key):
		return key in self

	def set(self, key, value):
		self[key] = value
		return self

	def delete(self, key):
		exists = key in self
		if exists:
			del self[key]

		return exists