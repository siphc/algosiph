import math


class Segtree:
    def __init__(self, a: list, mode: str) -> None:
        self.n = len(a)
        self.a = a

        d = {"sum": 0,
             "max": -float('inf'),
             "min": float('inf'),
             "gcd": 0,
             "lcm": 1}

        # dummy value to make no changes during an operation
        self.num = d[mode]

        # acceptable values: sum, min, max, gcd, lcm
        self.mode = mode

        # array used to represent the tree has length 4n
        # some won't be used; represented by float('inf')
        self.tree = [float('inf') for _ in range(4*len(a))]

    # helper method
    def _calc(self, a: int, b: int) -> int:
        if self.mode == "sum":
            return a + b
        elif self.mode == "max":
            return max(a, b)
        elif self.mode == "min":
            return min(a, b)
        elif self.mode == "gcd":
            return math.gcd(a, b)
        elif self.mode == "lcm":
            return (a*b) // math.gcd(a, b)

    # can't use instance variables as function default parameters
    def _trcheck(self, tr: int) -> int:
        if tr == -1:
            return self.n-1
        return tr

    def build(self, idx=1, tl=0, tr=-1) -> None:
        # constructs segtree from array a
        tr = self._trcheck(tr)

        if tl == tr:
            self.tree[idx] = self.a[tl]
            return
        tm = (tl+tr)//2
        self.build(idx*2, tl, tm)
        self.build(idx*2+1, tm+1, tr)
        self.tree[idx] = self._calc(self.tree[idx*2], self.tree[idx*2+1])

    # both getres() and update() are based on INDEX in the ORIGINAL ARRAY A
    # 0-indexed
    def getres(self, l: int, r: int, idx=1, tl=0, tr=-1) -> int:
        # finds res of a[l,r]
        tr = self._trcheck(tr)

        if l > r:
            return self.num
        if tl == l and tr == r:
            return self.tree[idx]
        tm = (tl+tr)//2
        return self._calc(self.getres(l, min(r, tm), idx*2, tl, tm), self.getres(max(l, tm+1), r, idx*2+1, tm+1, tr))

    def update(self, newidx: int, newval: int, idx=1, tl=0, tr=-1) -> None:
        # dynamically updates self.tree to maintain segtree
        # use index in a as newidx
        tr = self._trcheck(tr)

        if tl == tr:
            self.tree[idx] = newval
            return
        tm = (tl+tr)//2
        if newidx <= tm:
            self.update(newidx, newval, idx*2, tl, tm)
        else:
            self.update(newidx, newval, idx*2+1, tm+1, tr)
        self.tree[idx] = self._calc(self.tree[idx*2], self.tree[idx*2+1])


obj = Segtree([1, 2, 3, 4, -1, 6, 7, 8, 9], "sum")
obj.build()
print(obj.tree)
print(obj.getres(6, 8))
obj.update(8, 0)
print(obj.getres(6, 8))
