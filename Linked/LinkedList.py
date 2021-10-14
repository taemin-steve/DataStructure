class LinkedList: #LinkedList의 장점은 worst case 에서도 O(1)의 성늘을 보일 수 있다는 것이다. 
#------------------------------------------Node---------------------------------------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self,element, next):
            self._element = element
            self._next = next
#-------------------------------------------------------------------------------------------------------
    
    def __init__(self):
        self._head = None #생성 당시에는 첫 노드가 없으으로 들어가지 않는다. 
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        if self.is_empty():
            raise EOFError('stack is empty')
        return self._head._element

    def pop(self): # Head에 있는 값을 꺼냄
        if self.is_empty():
            raise EOFError('stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

