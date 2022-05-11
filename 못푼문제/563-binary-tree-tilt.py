'''
0110 ~  못풀음 

이문제 어렵네요. 

구현이 어려웠음. 

Runtime: 88 ms, faster than 39.64% of Python3 online submissions for Binary Tree Tilt.
Memory Usage: 16.3 MB, less than 80.73% of Python3 online submissions for Binary Tree Tilt.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_of_tilt = 0
        # 모든 트리 노드의 tilt 의 합을 반환하라. 
        def dfs(node):
            nonlocal sum_of_tilt
            if not node:
                return 0 
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            tilt = abs(left_sum - right_sum)
            sum_of_tilt += tilt
            return left_sum + right_sum + node.val
        
        dfs(root)
        
        return sum_of_tilt 
    