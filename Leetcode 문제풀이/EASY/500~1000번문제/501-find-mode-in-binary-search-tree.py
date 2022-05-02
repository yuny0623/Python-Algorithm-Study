'''
0400 ~ 0417 

Runtime: 63 ms, faster than 73.48% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.5 MB, less than 41.95% of Python3 online submissions for Find Mode in Binary Search Tree.

딕셔너리에서 key, value 페어로 얻고 싶으면 d.items() 사용하자. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root.val == 0:
            return [0]

        d = dict() 
        def inorder(node):
            nonlocal d 
            if node.val == None:
                return 
            if node.val in d:
                d[node.val] += 1
            else:
                d[node.val] = 1 
            if node.left != None:
                inorder(node.left)
            if node.right != None:
                inorder(node.right)
                
                
        inorder(root)
        result = [] 
        most_freq = max(list(d.values()))
        for key, value in d.items():
            if value == most_freq:
                result.append(key)
        
        return result 
        
        