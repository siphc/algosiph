import math


class Segtree:
    def __init__(self, a: list, mode: str) -> None:
        self.n = len(a)
        self.a = a
        
        if mode == "sum":
            self.num = 0
        elif mode == "max":
            self.num = -float('inf')
        elif mode == "min":
            self.num = float('inf')
        elif mode == "gcd":
            self.num = 0
        elif mode == "lcm":
            self.num = 1

        # acceptable values: sum, min, max, gcd, lcm
        self.mode = mode

        # array used to represent the tree has length 4n
        # some won't be used; represented by float('inf')
        self.tree = [float('inf') for _ in range(4*len(a))]

    # helper method
    def calc(self, a: int, b: int) -> int:
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

    def build(self, idx: int, tl: int, tr: int) -> None:
        # constructs segtree from array a
        # default values that should be used outside of this function:
            # idx = 1
            # tl = 0
            # tr = n-1
        if tl == tr:
            self.tree[idx] = self.a[tl]
            return
        tm = (tl+tr)//2
        self.build(idx*2, tl, tm)
        self.build(idx*2+1, tm+1, tr)
        self.tree[idx] = self.calc(self.tree[idx*2], self.tree[idx*2+1])

    def getres(self, idx, tl, tr, l: int, r: int) -> int:
        # finds res of a[l,r]
        if l > r:
            return self.num
        if tl == l and tr == r:
            return self.tree[idx]
        tm = (tl+tr)//2
        return self.calc(self.getres(idx*2, tl, tm, l, min(r, tm)), self.getres(idx*2+1, tm+1, tr, max(l, tm+1), r))

    def update(self, idx, tl, tr, newidx: int, newval: int) -> None:
        # dynamically updates self.tree to maintain segtree
        # use index in a as newidx
        if tl == tr:
            self.tree[idx] = newval
            return
        tm = (tl+tr)//2
        if newidx <= tm:
            self.update(idx*2, tl, tm, newidx, newval)
        else:
            self.update(idx*2+1, tm+1, tr, newidx, newval)
        self.tree[idx] = self.calc(self.tree[idx*2], self.tree[idx*2+1])



# sample code

# obj = Segtree([1, 2, 3, 4, -1, 6, 7, 8, 9], "min")
# obj.build(1, 0, 8)
# print(obj.tree)
# print(obj.getres(1, 0, 8, 6, 8))
# obj.update(1, 0, 8, 8, 0)
# print(obj.getres(1, 0, 8, 6, 8))