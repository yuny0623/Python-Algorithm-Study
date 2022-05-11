'''
0430  ~ 0443 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        result = [] 
        def inorder(node, n):
            n += 1
            if node == None:
                return 
            if node.left == None and node.right == None:
                result.append(n)
            # result.append(n)
            if node.left != None:
                inorder(node.left, n)
            if node.right != None:
                inorder(node.right, n)
        
        inorder(root, cnt)
        if len(result) == 0:
            return 0 
        return min(result)