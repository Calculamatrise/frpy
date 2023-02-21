from .BaseManager import BaseManager

class CosmeticManager(BaseManager):
	def buy(self):
		response = self.client.post('/store/buy')
		if response.get('result') != False:
			self.client.user.stats['headCount'] += 1
			data = response.get('data')
			return data.get('head_gear')

	def set(self, item):
		self.client.post('/store/equip', data = {
            'item_id': item
        });
		return True