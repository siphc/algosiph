import java.util.*;

class TreeNode{
    int value;
    ArrayList<TreeNode> children;

    TreeNode(int v){
        value = v;
        children = new ArrayList<>();
    }
}

class BTreeNode{
    int value;
    BTreeNode left;
    BTreeNode right;

    BTreeNode(int v){
        value = v;
        left = right = null;
    }
}

class SLL{
    int value;
    SLL next;

    SLL(int v){
        value = v;
        next = null;
    }
}

class DLL{
    int value;
    DLL prev;
    DLL next;

    DLL(int v){
        value = v;
        prev = next = null;
    }
}