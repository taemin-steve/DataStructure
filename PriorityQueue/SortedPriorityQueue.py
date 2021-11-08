from Linked.PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase

class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)
    
    def min(self):
        if self.is_empty():
            raise InterruptedError("NO EMPTY")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise InterruptedError("NO EMPTY")
        item = self._data.delete(self._data.first()) #이미 정렬되어 있으므로 가장 앞에 것을 빼주면 해결
        return (item._key, item._value)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
