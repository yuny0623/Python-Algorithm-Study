'''
0404 ~  못풀었음. 

서브트리 확인 문제 

문제에 함정이 있음. subRoot 와 정확히 동일해야함. 즉 밑에 leaf 라던지 더 달려있는거
허용안됨. 딱 subRoot 모양 그대로 만 가능 

Runtime: 205 ms, faster than 24.29% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 15.1 MB, less than 63.74% of Python3 online submissions for Subtree of Another Tree.
''' 


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
    def sameTree(self, tree1, tree2):    
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2 and tree1.val==tree2.val:
            return (self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right))
        return False
