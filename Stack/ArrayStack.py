class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0 # 이렇게 하면 바로 boolean 값으로 값을 되돌려준다 
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty:
            raise RuntimeError("그만")
        return self._data[-1] #파이썬에서는 -1 하면 알아서 맨 마지막 인덱스로 접근
    
    def pop(self):
        if self.is_empty():
            raise RuntimeError("그만")
        return self._data.pop()


def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    s = ArrayStack()
    for c in expr :
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()

if __name__ == '__main__':
    print(is_matched("{야이자식아[}"))

    