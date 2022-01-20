# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# CODE 1
class Solution:
    def inorder(self, root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            arr = self.inorder(root)
            sum = 0
            for i in range(len(arr)):
                if arr[i] >= low and arr[i] <= high:
                    sum += arr[i]
            return sum




# CODE 2
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val<low:
                return self.rangeSumBST(root.right,low,high)
            elif root.val>high:
                return self.rangeSumBST(root.left,low,high)
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        else:
            return 0
