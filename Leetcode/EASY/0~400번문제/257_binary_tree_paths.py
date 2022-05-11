from typing import Optional, TreeNode, List
'''
1113 ~ 1134 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = [] 
        
        def preorder(node, s):
            if node == None:
                return 
            if node.left == None and node.right == None:
                result.append(s + str(node.val))
                return
            preorder(node.left, s+str(node.val) + '->')
            preorder(node.right,s+str(node.val) + '->')
            
        preorder(root, "")
        r = list(set(result))
        return r


