class ArrayQueue: # 작은 인덱스에서 부터 채워지고, 마지막에서 뺀다. 단, 여기서는 시작지점을 계속 순환시켜줌.
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY # 지정한 기본크기만큼의 None으로 초기화된 배열을 만들겠다.
        self._size = 0 # 배열의 실제 크기를 저장
        self._front = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise EOFError("그만")
        return self._data[self._front]
    
    def dequeue(self): #맨 앞에꺼를 꺼내는 메소드 
        if self.is_empty():
            raise EOFError("그만")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self, cap):
        old = self._data
        self._data = None*[cap]
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0

