# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return 
            self.inorder(root.right)
        
       
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0
        self.inorder(root)
        return self.res
