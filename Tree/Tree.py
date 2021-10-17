class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        
        def __nq__(self,other):
            return not(self == other)

        def root(self):
            raise NotImplementedError('must be implemented by subclass')

        def parent(self, p):
            raise NotImplementedError('must be implemented by subclass')

        def num_children(self,p):
            raise NotImplementedError('must be implemented by subclass')
        
        def children(self, p):
            raise NotImplementedError('must be implemented by subclass')
        
        def __len__(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def is_root(self,p):
            return.self.root() == p
        
        def is_leaf(self,p):
            return self.num_childern(p) == 0
        
        def is_empty(self):
            return len(self) == 0
