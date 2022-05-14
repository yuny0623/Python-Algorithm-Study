'''
0306 ~ 0306

Runtime: 148 ms, faster than 5.03% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 16.6 MB, less than 18.16% of Python3 online submissions for Search in a Binary Search Tree.

코멘트: 
어렵지 않은 문제 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pos = None
        def preorder(node):
            nonlocal pos 
            if node.val == val:
                pos = node 
            if node.left != None:
                preorder(node.left)
            if node.right != None:
                preorder(node.right)
                
        preorder(root)
        return pos 