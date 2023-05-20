import java.util.*;

// this is only integer!!
class DSU {
    private ArrayList<Integer> parent; // value is the immediate parent of the node (not the head of the tree)
    // this might also be much faster if i just use an array and tailor to the problem bounds ffs
    private ArrayList<Integer> depth;

    public DSU(){
        parent = new ArrayList<Integer>();
        depth = new ArrayList<Integer>();
    }

    public void makeSet(int i) {
        parent.set(i, i);
        depth.set(i, 1);
    }

    public int find(int i) { // finds parent node of the num
        if (parent.get(i) == i) {
            return i;
        }
        return parent.set(i, find(parent.get(i)));
    }

    public void union(int a, int b) { // attachs b to a
        a = find(a);
        b = find(b);
        if (a!=b) {
            if (depth.get(a) < depth.get(b)) { // if a has a shorter tree than b, attach a to b instead
                // grrr why no swap()
                int c = a;
                a = b;
                b = c;
            }
            parent.set(b, a); // this is the actual attachment
            if (depth.get(a) == depth.get(b)) {
                depth.set(a, depth.get(a)+1);
            }
        }
    }
}