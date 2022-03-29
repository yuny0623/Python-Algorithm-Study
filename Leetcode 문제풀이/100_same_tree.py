'''
1205 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def inorder(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False 
            if p.val == q.val:
                return inorder(p.left,q.left) and inorder(p.right, q.right)
            
        
        return inorder(p, q)
        
        




