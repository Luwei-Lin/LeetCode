#include <iostream>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    vector<int> vi;
    TreeNode* head = new TreeNode();
public:
    TreeNode* increasingBST(TreeNode* root) {
        if (!root) return root;
        inorderTraversal(root);
        TreeNode *temp = head;
        for (auto v: vi){
            temp->right = new TreeNode(v);
            temp = temp->right; 
        }
        return head->right;
    }
    void inorderTraversal(TreeNode* root){
        if (!root) return;
        increasingBST(root->left);
        vi.push_back(root->val);
        increasingBST(root->right);
    }
    TreeNode* cur = NULL;
    TreeNode* increasingBST_2(TreeNode* root){
        TreeNode* preHead = new TreeNode(-1);
        cur = preHead;
        inorderTraversal2(root);
        return preHead->right;
    }
    void inorderTraversal2(TreeNode* root){
        if(!root) return;
        inorderTraversal2(root->left);
        root->left = NULL;
        cur->right = root;
        cur = cur->right;
        inorderTraversal2(root->right);
    }
};

void inorder(TreeNode *root){

    if (root == nullptr) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
    
}

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

int main(){

    string A[] = {"5","3","6","2","4","null","8","1","null","null","null","7","9"};
    TreeNode* root = new TreeNode();
    TreeNode* newRoot = new TreeNode();
    int size = sizeof(A)/sizeof(A[0]);
    root = createTree(A, root, 0, size);
    Solution s;
    cout << "original: "<< endl;
    level(root);
    newRoot = s.increasingBST_2(root);
    cout << "new:" <<endl;
    level(newRoot);
    return 0;
}