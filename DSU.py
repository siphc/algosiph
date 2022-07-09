# DSU initiated using existing dict.
# dict shall be created with key=value.
class DSU:
    def __init__(self, d: dict) -> None:
        self.parent = d  # key=node, value=parent
        self.depth = {}  # key=node, value=size
        # keep in mind only parent nodes are used in self.depth
        for k, v in self.parent.items():
            self.depth[k] = 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # the order of a and b does not matter
    def union(self, a, b) -> None:
        a = self.find(a)
        b = self.find(b)
        if a != b:
            # union by depth
            if self.depth[a] < self.depth[b]:
                a, b = b, a
            self.parent[b] = a
            if self.depth[a] == self.depth[b]:
                self.depth[a] += 1



# DSU with elements added dynamically.
# syntax:
# obj = DSU_Dynamic()
# obj.add(2)
# obj.add(3)
# obj.union(3,2)
# this shall create the tree 3->2.
class DSU_Dynamic:
    def __init__(self) -> None:
        self.parent = {}
        self.depth = {}

    def add(self, x) -> None:
        # manually union!
        self.parent[x] = x
        self.depth[x] = 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b) -> None:
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.depth[a] < self.depth[b]:
                a, b = b, a
            self.parent[b] = a
            if self.depth[a] == self.depth[b]:
                self.depth[a] += 1
