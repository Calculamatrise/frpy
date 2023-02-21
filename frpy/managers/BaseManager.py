from ..utils.Map import Map

class BaseManager:
	cache = Map()
	def __init__(self, parent):
		self.client = parent