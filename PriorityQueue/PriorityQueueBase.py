class PriorityQueueBase:

#------------------------------------------------------------------
    class _Item:

        __slots__ = '_key', '_value'

        def __init__(self,k ,v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)
#------------------------------------------------------------------

    def is_empty(self):
        return len(self) == 0
    
            