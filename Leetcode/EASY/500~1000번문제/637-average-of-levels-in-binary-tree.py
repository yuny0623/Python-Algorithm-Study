'''
0358 ~ 0437 <답지 보고 풀음ㅠ>
Runtime: 71 ms, faster than 46.45% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.6 MB, less than 45.36% of Python3 online submissions for Average of Levels in Binary Tree.

bfs 문제였음. 
bfs = 큐 <- 그냥 큐로 풀면 다풀림. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            avg_list = []     
            for i in range(size):
                n = queue.pop(0)
                avg_list.append(n.val)
                if n.left != None:
                    queue.append(n.left)
                if n.right != None:
                    queue.append(n.right)
                
            result.append(sum(avg_list) / size)
        return result 
                
            
            


