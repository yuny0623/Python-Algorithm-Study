'''
1005  ~1014 
Runtime: 95 ms, faster than 13.94% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.4 MB, less than 14.83% of Python3 online submissions for N-ary Tree Preorder Traversal.

이문제는 원래는 쉬운문제인데 타입이 어떻게 들어가있는지를 헷갈려서 조금 고민했다. 
children 은 list 인데 그 list 안에 Node 클래스 타입으로 객체들이 요소로 들어가있는거다  
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return [] 
        result = [root.val]
        def pre(node):
            if node == None:
                return 
            for child in node.children:
                result.append(child.val)
                pre(child)
                
        pre(root)
        return result 
            
                

