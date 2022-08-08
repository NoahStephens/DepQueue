from queue import PriorityQueue

class DepQueue:
	""" A doubly ended priority queue. """
	def __init__(self, maxsize=-1):
		self._maxsize = maxsize
		self._queue = PriorityQueue(self._maxsize)
		self._count = 0
		print(type(self).__name__)

	def get(self, block=True, timeout=None):
		return self._queue.get(block, timeout)

	def task_done(self):
		return self._queue.task_done()

	def join(self):
		return self._queue.join()

	def qsize(self):
		return self._queue.qsize()

	def full(self):
		return self._queue.full()

	def _reorder_queue(self):
		""" Shifts all prioritys in the queue. """

		""" checks if a reorder is needed. """
		(_item, _key) = self._queue.get(False)
		self._queue.put((_item, _key))
		self._queue.task_done()
		if (_key != None and _key > 2):
			print("Bail")
			return

		queue = PriorityQueue(self._maxsize)
		while self._queue.qsize() > 0:
			(item, key) = self._queue.get(False)
			key = key + 1
			queue.put((item, key))
			self._queue.task_done()
		

		self._queue = queue

	def put(self, item, priority=1, block=True, timeout=None):
		""" Puts an item in the queue. 
		If the priority is greater than 0 or not given the item is placed at the end of the queue. 
		If the priority is less than 0 or 0 the item is placed at the beginning of the queue. """
		self._count = self._count + 1

		if (priority <= 0):
			self._reorder_queue()
			self._queue.put((item, 1), block, timeout)
		else:
			self._queue.put((item, self._count), block, timeout)

if __name__ == '__main__':
	dep = DepQueue(100)
	dep.put("dog")
	dep.put("cat")
	dep.put("moo cow", 0)


	print(dep.get())