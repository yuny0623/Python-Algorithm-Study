'''
0240 ~ 0307  <답지보고 풀음>
Runtime: 163 ms, faster than 12.94% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.7 MB, less than 20.39% of Python3 online submissions for Merge Two Binary Trees.

트리 두개 머지하는 문제. 문제가 좋음. 좋은문제.  
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 두 트리 합치세요 
        # 두 노드 겹치면? 합을 넣으세요 
        # 근데 트리 두개를 동시에 순회해야할것 같음. 
        # 즉 그냥 preorder 같은걸로 트리 순회가 아니라 
        # dfs로 반복문으로 돌면서 풀어야할 것 같은데... 
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 if root1 else root2
        
        
            



