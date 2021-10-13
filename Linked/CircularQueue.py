class CircularQueue:

    class _Node:
        __slots__ = '_element','_next'
        def __intit__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('비었습니다')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('비었습니다')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail._next = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
        
