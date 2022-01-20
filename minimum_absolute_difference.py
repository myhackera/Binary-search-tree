# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:    
            return None
        output = self.inorder(root)
        min_diff = 1000
        for i in range(1, len(output)):
            min_diff = min(min_diff, output[i]-output[i-1])
        return min_diff
       
