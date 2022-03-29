# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def inorder(node, n):
            if node == None:
                return 
            n += 1
            result.append(n)
            if node.left != None:
                inorder(node.left, n)
            if node.right != None:
                inorder(node.right, n)

        result = []
        cnt_node = 0
        inorder(root, cnt_node)
        if len(result) == 0:
            return 0
        else: 
            return max(result)