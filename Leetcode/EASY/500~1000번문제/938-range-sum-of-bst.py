'''
0525 ~ 0531 

코멘트: 
그냥 구현하면 풀림. 딱히 어렵진 않음.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        result = 0 
        def inorder(node):
            nonlocal result 
            if low <= node.val <= high:
                result += node.val
            if node.left != None:
                inorder(node.left)
            if node.right!= None:
                inorder(node.right)
        
        inorder(root)
        
        return result 