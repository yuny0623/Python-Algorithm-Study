'''
0326 ~ 0351 
Runtime: 102 ms, faster than 5.43% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 16 MB, less than 92.82% of Python3 online submissions for Maximum Depth of N-ary Tree.

코멘트: 
데이터 타입이 어떻게 되는지 조금 구체적이지 않음. 
리스트 타입으로 children 이 주어지는가? 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0 
        #  each group of children is separated by the null value 
        max_depth = 1

        def search(node, v):
            nonlocal max_depth 
            if node == None:
                return 
            if len(node.children) == 0:
                if max_depth < v:
                    max_depth = v
                return 
            if len(node.children) != 0:
                for i in range(len(node.children)):
                    search(node.children[i], v + 1)
        
        search(root, 1)
        return max_depth 

