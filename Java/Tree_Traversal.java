class BTreeNode{
    int value;
    BTreeNode left;
    BTreeNode right;

    BTreeNode(int v){
        value = v;
        left = right = null;
    }
}

public class Tree_Traversal {
    public static void preorder(BTreeNode node) {
        if (node==null) {
            return;
        }
        // operation!
        preorder(node.left);
        preorder(node.right);
    }
}