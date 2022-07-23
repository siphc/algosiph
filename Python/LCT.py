class LCT:
    def __init__(self):
        pass

    # helper function
    # make root-to-v path preferred, due to being last vertex accessed
    # make v root of its tree. 
    def access(self, v):
        pass

    # creates vertex v.
    def make_tree(self,v):
        pass

    # makes vertex v a child of w.
    # assumes v is the root of its tree.
    # assumes v and w are in distinct trees.
    def link(self, v, w):
        pass

    # deletes edge between v and its parent.
    # assumes v is not the root.
    def cut(self, v):
        pass

    # returns root node of the tree that v is a part of.
    # on average O(log n), but can be very long.
    def find_root(self, v):
        pass

    # returns aggregate of the path from v to v's root
    def path_aggregate(self, v):
        pass