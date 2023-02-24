from threading import Thread

class EventEmitter:
	__deprecated = set()
	__events = {}
	def emit(self, event, *args):
		if event not in self.__events: return
		threads = [Thread(target = listener, args = (self, *args)) for listener in self.__events[event]]
		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

		for listener in self.__events[event]:
			if id(listener) in self.__deprecated:
				self.__events[event].remove(listener)

	def on(self, event, listener):
		if not isinstance(event, str):
			raise TypeError("Event name must be type str!")
		elif not callable(listener):
			raise TypeError("Listener function must be callable!")

		if event not in self.__events:
			self.__events[event] = []

		self.__events[event].append(listener)
		return len(self.__events[event])

	def once(self, event, listener):
		length = self.on(event, listener)
		self.__deprecated.add(id(listener))
		return length

	def listeners(self, event):
		if event in self.__events:
			return len(self.__events[event])

		return 0

	def removeListener(self, event, listener):
		if event in self.__events:
			for savedListener in self.__events[event]:
				if savedListener == listener:
					self.__events[event].remove(listener)
					if len(self.__events[event]) < 1:
						del self.__events[event]

					return True

		return False

	def removeAllListeners(self, event):
		if event in self.__events:
			del self.__events[event]
			return True

		return False