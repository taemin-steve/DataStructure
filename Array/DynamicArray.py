import ctypes

class DynamicArray:
    def __init__(self):
        self._n =0
        self._capacity =1
        self._A = self._make_array(self._capacity) # 자신의 크기만큼 만들겠다? 이건 한번 일어나는거고. 

    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c): #이때 c는 리사이즈 할 크기. 
        B = self._make_array(c) #이때 c는 이미 두배 해서 들어오기 때문에 2배 크기의 어레이 생성
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B #다 옴긴다음에 다시 배열 주소를 넘겨줌
        self._capacity = c 
    
    def _make_array(self,c):
        return (c*ctypes.py_object)()  #이거는 그냥 파이썬 모듈이라고 생각합시당 
    
    def insert(self,k,value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    
    def remove(self,value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n -1] = None
                return
        raise ValueError('없다')

d = DynamicArray()
d.append(1)
print(d._capacity)
d.append(2)
print(d._capacity)
d.append(3)
print(d._capacity)
d.append(3)
print(d._capacity)



