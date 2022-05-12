'''
0226 ~ 0238 

딱히 어렵진 않음. 근데 중간에 숨어있는 조건이 하나있음.
근데 예시보고 그대로 구현하면됨. 함정없음. 
left 는 None인데 right는 요소가 없을 경우 빈 () 를 하나 추가해줘야함. 
<- 위 말 그대로 구현하면 됨. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        result = [] 
        def preorder(node):
            result.append(str(node.val))
            if node.left != None:
                result.append("(")
                preorder(node.left)
                result.append(")")
            if node.left == None and node.right != None:
                result.append("()")
            if node.right != None:
                result.append("(")
                preorder(node.right)
                result.append(")")

                
        preorder(root)
        return ''.join(result) 



