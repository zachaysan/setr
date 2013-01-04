from datetime import datetime

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

class FastRange(object):
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

class MultiRange(object):
    def __init__(self, ranges=None):
        self.ranges = ranges or []

    def add_range(self, r):
        """ Adds a comprising range and sorts based on min value. """
        self.ranges.append(r)
        self.ranges.sort(key=lambda r: min(r))
    
    def flatten(self):
        self.ranges = self.safely_flatten()

    def safely_flatten(self):
        new_ranges = []
        for r in self.ranges:
            new_ranges = [nr for nr in self._get_range_(new_ranges, r)]
        return MultiRange(new_ranges)

    def count_in(self, item):
        """ Counts the number of ranges that the compared item matches """
        return sum([item in r for r in self.ranges])

    def _get_range_(self, new_ranges, r):
        for nr in new_ranges:
            overlapping_range = self._overlapping_range_(r, nr)
            if overlapping_range:
                yield overlapping_range
                return
            yield nr
        yield r

    def _overlapping_range_(self, considered_range, prev_range):
        """ Considers a new range in a series of ranges.
        If there is overlap with the previous range it joins 
        the two.
        """
        if min(considered_range) in prev_range:
            m = max(max(considered_range), max(prev_range))
            return FastRange(min(prev_range), m)
        return False

    def __contains__(self, item):
        for r in self.ranges:
            if item in r:
                return True
        return False
    
    def __min__(self):
        return min([min(r) for r in self.ranges])
    
    def __max__(self):
        return max([max(r) for r in self.ranges])

class TimeRange(FastRange):
    def __init__(self, starting_date, time_delta=None, ending_date=None):
        if ending_date and time_delta:
            raise "TimeRange expects one of ending_date or time_delta (both supplied)"
        elif not (ending_date or time_delta):
            raise "TimeRange expects one of ending_date or time_delta (none supplied)"

        if not ending_date:
            ending_date = starting_date + time_delta

        n, m = int(starting_date.strftime("%s")), int(ending_date.strftime("%s"))
        super(TimeRange, self).__init__(n, m)
        
    def __contains__(self, item):
        return int(item.strftime("%s")) in super(TimeRange, self)
    
    def __max__(self, item):
        mx = max(super(TimeRange, self))
        return datetime.fromtimestamp(mx)

    def __min__(self, item):
        mn = min(super(TimeRange, self))
        return datetime.fromtimestamp(mn)
    
    def __iter__(self):
        for item in super(TimeRange, self):
            yield dateteim.fromtimestamp(item)

def main():
    # These should be testified. Heh.
    f = FastRange(20, 50)
    g = FastRange(60, 100)
    j = FastRange(80, 150)
    h = FastRange(90, 120)
    mr = MultiRange()
    mr.add_range(f)
    mr.add_range(g)
    mr.add_range(j)
    mr.add_range(h)
    print mr.count_in(93)
    print 55 in mr
    print 95 in mr
    print mr.__dict__
    mr2 = mr.safely_flatten()
    print mr2.__dict__
    for r in mr2.ranges:
        print r.__dict__

if __name__=='__main__':
    main()
