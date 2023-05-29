Class TreeNode{
    int value;
    TreeNode[] children;

    TreeNode(int v){
        value = v;
        children = new TreeNode[];
    }

    TreeNode(){
        value = 0;
        children = new TreeNode[];
    }
}