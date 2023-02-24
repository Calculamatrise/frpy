from .BaseManager import BaseManager
from ..structures.Cosmetic import Cosmetic
from ..utils.RequestHandler import RequestHandler

class CosmeticManager(BaseManager):
	__parent = None
	def __init__(self, parent, data):
		self.__parent = parent
		data = data or []
		if 'head' in data:
			self.head = Cosmetic(data.get('head'))

	def buy(self):
		response = RequestHandler.post('/store/buy')
		if response.get('result') != False:
			self.__parent.stats['headCount'] += 1
			data = response.get('data')
			return data.get('head_gear')

	def equip(self, item):
		return bool(RequestHandler.post('/store/equip', data = {
            'item_id': item
        }))