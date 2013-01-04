mx = max
mn = min

def max(item, *args):
    if hasattr(item, '__max__') and callable(item.__max__) and not len(args):
        return item.__max__()
    return mx(item, *args)

def min(item, *args):
    if hasattr(item, '__min__') and callable(item.__min__) and not len(args):
        return item.__min__()
    return mn(item, *args)

class FastRange:
    def __init__(self, n, m=None):
        if not m:
            self.m = n
            self.n = 0
        else:
            self.n = n
            self.m = m
        self.xrange = xrange(self.n, self.m)

    def __contains__(self, item):
        if item < self.n:
            return False
        if item >= self.m:
            return False
        return True

    def __iter__(self):
        for x in self.xrange:
            yield x
            
    def __len__(self):
        return len(self.xrange)

    def __max__(self):
        return self.m
    
    def __min__(self):
        return self.n
