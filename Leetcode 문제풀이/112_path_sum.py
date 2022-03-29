'''
0443 ~ 0513 

조건 충족했을때 flag 같은 변수로 체크해서 확인하는것보다 
아래 처럼 짜는게 오히려 더 가독성 좋음. 에러날 확률도 적고. 
global 써서 flag 기능으로 사용하는건 이제 쓰지 말자 별로네  
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def inorder(node, t):
            if node == None:
                return 
            t += node.val
            if node.left == None and node.right == None:
                if t == targetSum:
                    return True
                else: 
                    return False 
            
            return inorder(node.left, t) or inorder(node.right, t)
        
        total = 0 
        return inorder(root, total)
        
