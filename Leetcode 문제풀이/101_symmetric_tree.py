# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        side1 = root.left
        side2 = root.right 
        
        def inorder(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False 
            if p.val == q.val:
                return inorder(p.left, q.right) and inorder(p.right, q.left)
        
        return inorder(side1, side2)