from Linked.PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase

class UnsortedPriorityQueue(PriorityQueueBase):
    
    def __init__(self):
        self._data = PositionalList() # 포지셔널 리스트 == 결국 doublyLinked 형태를 이용하여 만들겠다.
    
    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value)) # 새로 만든 포지셔널 리스트에 마지막에 계속 해서 삽임.
    
    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)

#-------------------nonpublic behavior -----------------------------------------------------
    def _find_min(self):

        if self.is_empty():
            raise ValueError("No Empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None: #끝까지 돌면서 
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
        