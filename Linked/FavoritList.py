from PositionalList import PositionalList

class FavoritList:

    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0 
        
    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self,p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while(walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    def __init__(self):
        self._data = PositionalList()
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e)) # positional list에다가 item을 집어 넣겠다.
        p.element()._count += 1
        self._move_up(p) # 추가 되는 즉시 정렬을 거치겠다. 
    
    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
        
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("값이 틀렸습니다")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
        
    def __repr__(self):
        return ', '.join('({0}:{1})'.format(i._value, i._count) for i in self._data)