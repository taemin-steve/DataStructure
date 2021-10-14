from DoublyLinkedList import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):
#여기서 가로안에 다른 클래스를 받는것은 파이썬에서의 상속 문법이라고 할 수 있다. 

    def first(self):
        if self.is_empty():
            raise EOFError("잘못 입력하였습니다")
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise EOFError("잘못 입력하였습니다")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self,e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise EOFError("잘못 입력하였습니다")
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise EOFError("잘못 입력하였습니다")
        self._delete_node(self._trailer._prev)
    
