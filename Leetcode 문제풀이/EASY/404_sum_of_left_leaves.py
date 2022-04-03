'''
0200 ~ 0206 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        def preorder(node):
            nonlocal total 
            if node == None:
                return 
            if node.left != None:
                if node.left.right == None and node.left.left == None:
                    total += node.left.val
                else:
                    preorder(node.left)
            if node.right != None:
                preorder(node.right)
        
        preorder(root)
        return total 