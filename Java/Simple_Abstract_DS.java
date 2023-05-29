import java.util.*;

class TreeNode{
    int value;
    ArrayList<TreeNode> children;

    TreeNode(int v){
        value = v;
        children = new ArrayList<>();
    }

    TreeNode(){
        value = 0;
        children = new ArrayList<>();
    }
}