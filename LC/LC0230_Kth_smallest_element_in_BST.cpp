#include <iostream>
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

class Solution {
private:
    vector<int> vi;
public:
    void inorder(TreeNode* root){
        if(!root) return;
        inorder(root->left);
        vi.push_back(root->val);
        inorder(root->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        inorder(root);
        return vi[(unsigned long)k - 1];
    }
    int count = 0;
    int found = 0;
    int kthSmallest2(TreeNode* root, int k) {
        if (!root) return found;
        kthSmallest2(root->left, k);
        if (count++ == k - 1) {
            found = root->val;
            return found;
        }
        kthSmallest2(root->right, k);
        return found;
    }
    int kthSmallest3(TreeNode* root, int k){
        if(!root) return 0;
        stack<TreeNode*> st;
        
        while (!st.empty() || root != NULL){
            if(root !=  NULL) {
                st.push(root);
                root = root->left;
            } else {
                
                root = st.top(); st.pop();
                if (--k == 0) return root->val;
                root = root->right;
            }
        }
        return 0;
    }
};

void inorder(TreeNode *root){

    if (root == nullptr) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
    
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
    string A[] = {"5","3","6","2","4","null","null","1"};
    int k = 3;
    int size = sizeof(A)/sizeof(A[0]);
    TreeNode* root = new TreeNode();
    root = createTree(A, root, 0, size);
    cout << "original: "<< endl;
    inorder(root);
    cout <<endl;
    Solution s;
    cout << "the " << k << "th smallest:" << endl;
    cout << s.kthSmallest3(root, k) <<endl;
    return 0;
}