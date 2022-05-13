'''
0200   ~0203 
Runtime: 52 ms, faster than 21.32% of Python3 online submissions for Second Minimum Node In a Binary Tree.
Memory Usage: 13.8 MB, less than 65.92% of Python3 online submissions for Second Minimum Node In a Binary Tree.

코멘트: 
쉬운문제임. 근데 코드에서 함수콜 한번으로 second minimum 구할 수 있을까? 
뭔가 가능할 것 같은데 한번 해보자. 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        result = [] 
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            result.append(node.val)
            if node.right != None:
                inorder(node.right)
        
        inorder(root)
    
        li = sorted(list(set(result)))
        if len(li) == 1:
            return -1
        else:
            return li[1]

'''
개선한 솔루션: 
'''

