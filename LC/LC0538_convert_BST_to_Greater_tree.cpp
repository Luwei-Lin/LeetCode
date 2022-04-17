#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef unsigned long usint8;
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
//method one
    vector<int> sums;
    usint8 index = 0;
    //method 2
    int sum = 0;
    //method 3
public:
    
    void inOrderTraversal(TreeNode* root){
        if (root == nullptr) return;
        inOrderTraversal(root->left);
        sums.push_back(root->val);
        inOrderTraversal(root->right);
    }
    void inOrderUpdate(TreeNode* root){
        if(root == nullptr) return;
        inOrderUpdate(root->left);
        root->val = sums[index++];
        inOrderUpdate(root->right);
    }
    TreeNode* convertBST(TreeNode* root){
        inOrderTraversal(root);
        for (usint8 i = sums.size() - 1; i > 0 ; i--){
            sums[i - 1] += sums[i];
        }
        inOrderUpdate(root);
        return root;
    }

    
    TreeNode* convertBST_2(TreeNode* root){
        if (!root) return NULL;
        convertBST_2(root->right);
        sum += root->val;
        root->val = sum;
        convertBST_2(root->left);
        return root;
    }
    /*
    TreeNode* convertBST_3(TreeNode *root){
        //stack implement
        return nullptr;
    }
    */
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

TreeNode* createTree1(string A[], TreeNode *root, int i, int size){
    if (i < size){
        if (A[i] == "null") return nullptr;
        TreeNode *temp = new TreeNode(stoi(A[i]));
        root = temp;
        root->left = createTree1(A, root->left, 2 * i + 1, size);
        root->right = createTree1(A, root->right, 2 * i + 2, size);
    }
    return root;
}
/*
buggy
void createTree3(TreeNode* node, int i, const string A[], int size){
    if (node != nullptr){
            if (2 * i + 1 < size){
            if (A[2 * i + 1] == "null"){
                node->left = nullptr;
                } else {
                    node->left = new TreeNode(stoi(A[2 * i + 1]));
                }
                createTree3(node->left, 2 * i + 1, A, size);
                }
            if (2 * i + 2 < size){
                if (A[2 * i + 2] == "null"){
                    node->right = nullptr;
                } else {
                    node->right = new TreeNode(stoi(A[2 * i + 2]));
                }
                createTree3(node->left, 2 * i + 2, A, size);
            }
    }
}
TreeNode* levelOrderCreateTree(string A[], int size){
    if(size == 0) return nullptr;
    TreeNode* root = new TreeNode(stoi(A[0]));
    createTree3(root, 0, A, size);
    return root;
}
*/

int main(){
    
    //const int A[] = {4,1,6,0,2,5,7, NULL, NULL, NULL, 3, NULL, NULL, NULL, 8};
    //const char A[] = {'4', '1', '6', '0', '2', '5', '7', , NULL, NULL, NULL, '3', NULL, NULL, NULL, '8'};
    string A[] = {"4", "1", "6", "0", "2", "5", "7", "null", "null", "null", "3", "null", "null", "null", "8"};//this works
    int size = sizeof(A)/sizeof(A[0]);
    

    TreeNode* root = new TreeNode();
    //root = createTree(A, root, 0, size);
    root = createTree1(A, root, 0, size);
    //root = levelOrderCreateTree(A, size);//has bug

    cout << "original sequence: " << endl;
    level(root);
    
    //inorder(root); //print in order 
   // cout << endl;
    Solution s;
    //s.convertBST(root);
    s.convertBST_2(root);
    cout << "changed output" <<endl;
    level(root);

    return 0;
}