from ..utils.RequestHandler import RequestHandler

class Cosmetic:
	def __init__(self, data = {}):
		head = data.get('head') or data
		self.classname = head.get('classname')
		self.cost = head.get('cost') or 0
		self.equiped = head.get('equiped')
		self.id = head.get('id')
		self.img = head.get('img')
		self.limited = head.get('limited')
		self.name = head.get('name')
		self.script = head.get('script')
		self.show = head.get('show')
		self.spritesheetId = head.get('spritesheet_id')
		self.title = head.get('title')
		self.type = head.get('type')
		if 'options' in head:
			self.options = head.get('options')

	def equip(self):
		return bool(RequestHandler.post('/store/equip', True, data = {
            'item_id': self.id
        }))