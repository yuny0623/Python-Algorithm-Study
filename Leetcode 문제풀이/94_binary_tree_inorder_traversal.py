'''
1140 
~ 1202 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = [] 
        def in_order(node): # 중위 순회 
            if node == None:
                return
            if node.left != None:
                in_order(node.left)
            result.append(node.val)
            if node.right != None:
                in_order(node.right)
        
        in_order(root)
        return result 

        
        
        
        
        
        
        
        

