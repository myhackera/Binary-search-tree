# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TC : O(N) , SC : O(N)
class Solution:
    def inorder(self, root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = self.inorder(root)
        low = 0 
        high = len(res)-1
        while(low < high):
            if res[low]+res[high] == k:
                return True
            elif res[low]+res[high] > k:
                high -= 1
            else:
                low += 1 
        return False
      
# TC : O(N) , SC : O(log(N))   
class Solution:
    def target(self, root, nodes, k):
        if root is None:
            return False
        complement = k - root.val
        if complement in nodes:
            return True
        nodes.add(root.val)
        return self.target(root.left, nodes, k) or self.target(root.right, nodes, k)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return self.target(root, set(), k)
