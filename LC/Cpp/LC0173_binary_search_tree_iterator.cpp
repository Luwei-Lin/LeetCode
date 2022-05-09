#include <iostream>
#include <queue>
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
void level(TreeNode *root){
    if (root == nullptr) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()){
        cout << q.front()->val << " ";
        if (q.front()->left != NULL) q.push(q.front()->left);
        if (q.front()->right != NULL) q.push(q.front()->right);
        q.pop();
    }
    cout << endl;
}

TreeNode* createTree(string A[], TreeNode *root, int i, int size){
    if (i < size){
        if (A[i] == "null") return nullptr;
        TreeNode *temp = new TreeNode(stoi(A[i]));
        root = temp;
        root->left = createTree(A, root->left, 2 * i + 1, size);
        root->right = createTree(A, root->right, 2 * i + 2, size);
    }
    return root;
}
class BSTIterator {
private:
    stack<TreeNode*> st;
    vector<int> vt;
    int cur = 0;
public:
    void inorderVT(TreeNode* root){
        if(!root) return;
        inorderVT(root->left);
        vt.push_back(root->val);
        inorderVT(root->right);
    }
    BSTIterator(TreeNode* root) {
        inorderVT(root);
    }
    
    int next() {
        int res = 0;
        if(hasNext()){
            res = vt[cur++];
        }
        return res;
    }
    
    bool hasNext() {
        
        return cur < (int)vt.size();
    }
};

int main(){

    string A[] = {"7","3","15","null","null","9","20"};
    TreeNode* root = new TreeNode();
    int size = sizeof(A)/sizeof(A[0]);
    root = createTree(A, root, 0, size);
    cout << "original: "<< endl;
    level(root);

    BSTIterator* obj = new BSTIterator(root);
    int param_1 = obj->next();
    cout << param_1 <<endl;
    bool param_2 = obj->hasNext();
    cout << param_2 <<endl;
    int param_3 = obj->next();
    cout << param_3 <<endl;
    return 0;
}