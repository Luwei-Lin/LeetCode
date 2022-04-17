import queue
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        # low <= root.val <= high
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
    
def creatTree(data,index):
    pNode = None
    if index < len(data):
        if data[index] == None :
            return None
        pNode = TreeNode(data[index], creatTree(data, 2 * index + 1), creatTree(data, 2 * index + 2))
    return pNode  

def show(root):
    q = []
    if root == None:
        print(q)
    q.append(root)
    while len(q) != 0:
        temp = q.pop(0)
        if temp.val == None:
            print("None")
        print(temp.val)
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)
def main():
    
    data = [3,0,4,None,2,None,None, 1]
    root = creatTree(data, 0)
    
    show(root)
    low = 1
    high = 3
    newRoot = Solution().trimBST(root, low, high)
    show(newRoot)
    
main()