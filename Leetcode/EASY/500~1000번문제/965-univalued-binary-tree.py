'''
1037 ~ 1053 
Runtime: 39 ms, faster than 66.51% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 14 MB, less than 14.87% of Python3 online submissions for Univalued Binary Tree.
코멘트: 

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        uni = True 
        def isUni(node):
            nonlocal uni 
            if node.left != None:
                isUni(node.left)
            if node.val != val:
                uni = False
                return 
            if node.right != None:
                isUni(node.right)
        
        isUni(root)
        return uni 


