'''
0922 ~ 0945 

Runtime: 157 ms, faster than 21.09% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 20.2 MB, less than 13.86% of Python3 online submissions for Two Sum IV - Input is a BST.

투포인터 떠올렸으면 절반은 풀었음. -> 이라고 생각했지만 투포인터 안써도 되용 
투포인터로 풀려고 했다가 시간낭비함. 접근법이 완전 틀렸음. 
이의로 브루트 포스 문제였음. 설마 브루트포스일까 하고 그냥 다른 풀이로 진행했는데 브포 맞음.  ㅠ 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 투포인터!! 사용하면 될듯!! 
        result = []
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            result.append(node.val)
            if node.right != None:
                inorder(node.right)
            
        inorder(root)
        if len(result) == 1 and result[0] < k:
            return False 
        
        for i in range(len(result)):
            for j in range(i, len(result)):
                if i != j and result[i] + result[j] == k:
                    return True
        return False 
        
'''
중간에 조건문 없어도 되요 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 투포인터!! 사용하면 될듯!! 
        result = []
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            result.append(node.val)
            if node.right != None:
                inorder(node.right)
            
        inorder(root)
        
        for i in range(len(result)):
            for j in range(i, len(result)):
                if i != j and result[i] + result[j] == k:
                    return True
        return False 
            
        
