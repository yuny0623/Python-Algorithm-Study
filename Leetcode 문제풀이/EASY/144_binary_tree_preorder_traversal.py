from typing import Optional, List
'''
0930 ~ 0938 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = [] 
        
        def preorder(node):
            nonlocal result 
            if node == None:
                return 
            result.append(node.val)
            if node.left != None:
                preorder(node.left)
            if node.right != None:
                preorder(node.right)
        
        preorder(root)
        return result 