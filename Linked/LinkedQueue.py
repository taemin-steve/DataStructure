class LinkedQueue: # 먼저들어간 것은 head에 나중에 들어간것은 tail에 위치하게 된다. 오른쪽에서 왼쪽에 넣는다고 생각.
#------------------------------------------Node---------------------------------------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self,element, next):
            self._element = element
            self._next = next
#-------------------------------------------------------------------------------------------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("비어있어요")
        return self._head._element

    def dequeue(self): 
        #가장 먼저 들어간거 삭제. == 먼저들어간 것은 head에 존재. head 부터 삭제 하게된다. 
        if self.is_empty():
            raise Empty("비어있어요")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

         
