#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''

class Solution:
    def inorderSuccessor(self, root, x):
        succ = -1 
        while root != None:
            if x.data >= root.data:
                root = root.right
            else:
                succ = root
                root = root.left
        if succ != -1:
            return succ
        else:
            Node(-1)
