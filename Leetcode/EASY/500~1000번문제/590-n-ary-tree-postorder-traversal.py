'''
0807 ~ 0810 

Runtime: 89 ms, faster than 19.26% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16.3 MB, less than 48.38% of Python3 online submissions for N-ary Tree Postorder Traversal.

코멘트: 
어렵진 않은 문제. post()를 재귀호출하면서 post 호출 이후에 result 에 append 하는걸 postorder 구현으로 가져가는거임. 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return [] 
        result = []
        def post(node):
            nonlocal result
            if not node:
                return 
            for child in node.children:
                post(child)
                result.append(child.val)
        
        
        post(root)
        result.append(root.val)
        return result 


