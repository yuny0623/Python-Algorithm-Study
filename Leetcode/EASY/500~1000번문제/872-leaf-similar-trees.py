'''
0532 ~ 0537 
Runtime: 31 ms, faster than 92.21% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 14 MB, less than 47.66% of Python3 online submissions for Leaf-Similar Trees.

코멘트:
재밌는 문제임. 순회하기만 하면 그냥 풀 수 있는 문제. 쉬움. 
참고로 어차피 leaf 만 체크하면 되는거라 in, pre, post 어떤 order 이든 뭘쓰던 상관없음.  
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaf1 = []
        leaf2 = []
        def preorder(node, leaf):
            if node.left == None and node.right == None:
                leaf.append(node.val)
                return 
            if node.left != None:
                preorder(node.left, leaf)
            if node.right != None:
                preorder(node.right, leaf)
        
        preorder(root1, leaf1)
        preorder(root2, leaf2)
        
        return leaf1 == leaf2 