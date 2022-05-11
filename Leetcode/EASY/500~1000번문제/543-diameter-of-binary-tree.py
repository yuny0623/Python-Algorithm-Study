'''
0954 ~

https://www.youtube.com/watch?v=bkxqA8Rfv04
생각보다 어려움. 
답지 보고 풀었는데 아직도 제대로 이해가 안감. 
depth first search 문제임.  <- 이 문제는 다시 봐야함. 이해한건가 
'''
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]









