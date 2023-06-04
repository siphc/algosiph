import java.util.*;

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

// the premise is that the problem with nodes is settled in DSU already
// we just need to handle edges.
// there are two ways: class with compareTo(), or... just a 2d array lol

// OOP method:
class Edge implements Comparable{
    public int a, b;
    public Integer weight;

    public Edge(int a, int b, int weight){
        this.a = a; 
        this.b = b;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge e){
        return this.weight.compareTo(e.weight);
    }
}

public class Kruskal_DSU {
    public static void main(String[] args) {
        DSU MST = new DSU();
        int res = 0;
        ArrayList<Edge> result = new ArrayList<>();

        ArrayList<Edge> edges = new ArrayList<>();
        // should do some edge instantiation here
        edges.sort(); // this should work right?? i have a compareTo override right???

        // the numbering of nodes doesn't matter so we can just
        int n = 1234; // # of nodes
        for (int i = 0; i < n; i++) {
            MST.makeSet(i);
        }

        // behold, the entire algorithm:
        for (Edge e : edges) {
            if (MST.find(e.a) != MST.find(e.b)) {
                res += e.weight;
                result.add(e);
                MST.union(e.a, e.b);
            }
        }

        System.out.println(res);
        System.out.println(result);
    }
}