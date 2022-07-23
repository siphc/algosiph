template <typename T>
struct SLL{
    T val;
    SLL* next;
};

template <typename T>
struct DLL{
    T val;
    DLL* next, prev;
};

template <typename T>
struct BinaryTree{
    T val;
    BinaryTree* left;
    BinaryTree* right;
};

template <typename T>
struct Tree{
    T val;
    vector<Tree*> children;
};
