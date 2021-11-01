from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):   
            self._element = element
            self._parent = parent
            self._left = left
            self.right = right

    class Position(BinaryTree.Position):

        def __init__(self,container,node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self,other):
           return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(slef,node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self,p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self,p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    

    
    