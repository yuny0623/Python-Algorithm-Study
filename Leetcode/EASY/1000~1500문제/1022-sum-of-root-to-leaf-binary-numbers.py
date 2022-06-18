'''
0741 ~ 0758 

Runtime: 48 ms, faster than 69.93% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 14.3 MB, less than 7.97% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

코멘트: 
왜 안풀릴까.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum_of_leaf = 0
        def preorder(node, binary):
            nonlocal sum_of_leaf 
            if node.left == None and node.right == None:
                sum_of_leaf += int(binary + str(node.val), 2)
            if node.left != None:
                preorder(node.left, binary + str(node.val))
            if node.right != None:
                preorder(node.right, binary + str(node.val))
        preorder(root, '')
        
        return sum_of_leaf 

