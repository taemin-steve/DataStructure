from DoublyLinkedList import _DoublyLinkedBase
# position 객체를 만들어서 각각의 노드의 주
class PositionalList(_DoublyLinkedBase):

#-----------------------------------------------------------------------------------------
    class Position:
        def __init__(self, container, node):
            self._container = container # 이때 사용하는 것을보면 PositionalList의 주소를 저장해준다. 
            self._node = node
    
        def element(self):
            return self._node._element

        def __eq__(self, other):
            return (type(other) is type(self)) and (other._node is self._node)
            # is 는 동일한 객체를 가리키면 참을 반환한다. 
            #그럼 포지션 객체이고 컨테이너가 다르더라도 노드가 같으면 인정 하겠다는 것인가?
        
        def __ne__(self, other):
            return not (self == other)
            # 위에거의 반대 타입인데 이건 왜 이렇게 심플하게 적고 끝내는거지? 
#-----------------------------------------------------------------------------------------

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p는 반드시 포지션의 객채여야 합니다.')
        if p._container is not self: 
            raise ValueError('p dose not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self,node):
        if node is self._header or node is self._header:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter_(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    #________________________________________________________________

    def _insert_between(self, e , predecessor, successor): #원하는 곳에 넣어주고 포지션 객체를 리턴해준다. 
        node = super()._insert_between(e, predecessor, successor) # 새로 만든 노드를 리턴해준다. 
        return self._make_position(node) 

    def add_first(self, e):
        return self._insert_between(e,self._header,self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p ,e): #p는 기준 노드의 포지션, e는 값
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p , e):
       original = self._make_position(p)
       old_value = original._element
       original._element = e
       return old_value
