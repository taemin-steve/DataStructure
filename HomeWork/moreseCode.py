#Tree class===================================================================================
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        
        def __nq__(self,other):
            return not(self == other)
        
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
        
    def is_root(self,p):
        return self.root() == p
        
    def is_empty(self):
        return len(self) == 0

#===================================================================================================

#binaryTree=========================================================================================
class BinaryTree(Tree):
    
    def lef(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
#====================================================================================================

#LinkedBinaryTree=====================================================================================
class LinkedBinaryTree(BinaryTree):
    
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):   
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

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

    def _make_position(self,node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def _add_root(self,e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p ,e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left Child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
        
    def _add_right(self, p ,e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right Child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def decoding(self, p, morseList): 
        # 디코딩을 위해 추가한 메서드. p는 포지션을, morseList는 인코딩된 문자열은 보관하는 queue의 역할을 수행.
        # 재귀 호출을 진행할 때마다 복잡도가 절반으로 감소.
        node = self._validate(p)
        if len(morseList) == 0: #만약 morseList 의 크기가 0 이라면 원하는 노드에 도착.
            return self._make_position(node)
        x = morseList.pop(0) #morseList에 남아 있는 문자열중 가장 앞의 문자를 x에 저장
        if x == ".": # x 가 '.' 이라면 원하는 노드의 위치가 왼쪽임으로 node._left의 position과 남은 문자열로 재귀호출
            return self.decoding(self._make_position(node._left), morseList)
        else: # x 가 '-' 이라면 원하는 노드의 위치가 오른쪽임으로 node._left의 position과 남은 문자열로 재귀호출
            return self.decoding(self._make_position(node._right), morseList)
        
#=====================================================================================================


### 모르스 부호 TABLE==================================================================================
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'),
    ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'),
    ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'),
    ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'),
]
#======================================================================================================
#바이너리 트리 생성. 
# 생성기준은 left 노드에는 부모의 문자열뒤에 '.'을 추가한 문자열을, right 노드에는 
# 부모의 문자열 뒤에 '-'을 추가한 문자열을 저장.

t = LinkedBinaryTree() #미리 구현된 바이네리 트리를 생성

node0 = t._add_root(None) # 위에 명시한 기준으로 바이너리 트리생성
node1 = t._add_left(node0, table[ord("E")- 65]) #morseCode = .
node2 = t._add_right(node0, table[ord("T")- 65]) #morseCode = -

node3 = t._add_left(node1, table[ord("I")- 65]) #morseCode = ..
node4 = t._add_right(node1, table[ord("A")- 65]) #morseCode = .-

node5 = t._add_left(node2, table[ord("N")- 65]) #morseCode = -.
node6 = t._add_right(node2, table[ord("M")- 65]) #morseCode = --

node7 = t._add_left(node3, table[ord("S")- 65]) #...
node8 = t._add_right(node3, table[ord("U")- 65])

node9 = t._add_left(node4, table[ord("R")- 65])
node10 = t._add_right(node4, table[ord("W")- 65])

node11 = t._add_left(node5, table[ord("D")- 65])
node12 = t._add_right(node5, table[ord("K")- 65])

node13 = t._add_left(node6, table[ord("G")- 65])
node14 = t._add_right(node6, table[ord("O")- 65])

node15 = t._add_left(node7, table[ord("H")- 65])
node16 = t._add_right(node7, table[ord("V")- 65])

node17 = t._add_left(node8, table[ord("F")- 65])
#node18 = not exist

node19 = t._add_left(node9, table[ord("L")- 65])
#node20 = not exist

node21 = t._add_left(node10, table[ord("P")- 65])
node22 = t._add_right(node10, table[ord("J")- 65])

node23 = t._add_left(node11, table[ord("B")- 65])
node24 = t._add_right(node11, table[ord("X")- 65])

node25 = t._add_left(node12, table[ord("C")- 65])
node26 = t._add_right(node12, table[ord("Y")- 65])

node27 = t._add_left(node13, table[ord("Z")- 65])
node28 = t._add_right(node13, table[ord("Q")- 65])

#==============================================================

#==============================================================

def moreseCodeChange(arr): 
    #모르스 부호를 인코딩하고 디코딩하는 함수. 
    
    encodingList = []
    for word in arr: #arr 에 존재하는 모든 단어에 대하여 반복.
        if (ord(word) < 65) or (ord(word) > 90):
            raise ValueError("영문 대문자만 입력 가능합니다!")
        encodingList.append(table[ord(word) - 65][1]) #아스키 코드를 이용하여 해당 문자가 적힌 튜플에 접근
                                                     # 튜플의 인덱스를 통하여 morseCode를 얻고 그대로 
                                                     # encodingList에 append하여 추가해준다.
                                                     # 인덱싱을 이용하여 바로 접근하여 복잡도는 O(1)
    
    print("Morse Code:  " ,end="")
    print(encodingList)

    decodingList = [] #디코딩된 문자를 저장하기 위한 리스트. 

    for morseCode in encodingList: # encodingList에 존재하는 모든 element에 대하여 반복
        morseList = list(morseCode) #문자열로 저장되어 있는 morseCode를 리스트로 바꾸어서 저장
        decodingList.append(t.decoding(node0,morseList).element()[0]) # LinkedBinaryTree 에 구현해 놓은 decoding
                                                                      # 함수에 root의 position과 morseList전달.

    result = "".join(decodingList)
    print("Decoding  : " ,end="")
    print(result)


def main():
    print("입력 문장 : " ,end="")
    arr = input()
    moreseCodeChange(arr)

if __name__ == "__main__":
    	main()

    
