'''
1201 ~ <밥먹고옴> ~ 0111 

Runtime: 62 ms, faster than 14.72% of Python3 online submissions for Cousins in Binary Tree.
Memory Usage: 14.1 MB, less than 10.11% of Python3 online submissions for Cousins in Binary Tree.

코멘트: 
문제 자체는 상당히좋은 문제임. 다만 처음 보는 유형이라 바로 떠오르지 않음. 

코드가 꽤 길어졌다. 이 솔루션이 정해인지는 모르겠지만 나름 오래걸렸음에도 쉽게 느껴진 문제. 
풀이를 떠올리는게 어려운 문제가 아니다. 어떻게 풀지는 쉽게 알 수 있는데, 그걸 구현하는 과정에서 
체크해야할 것들이 좀 있어서 코드가 길어진다. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_depth = 0
        y_depth = 0
        x_parent = None
        y_parent = None
        previous_node_val = root.val
        
        def inorder(node, v, depth, x_or_y):
            nonlocal previous_node_val
            nonlocal x_depth
            nonlocal y_depth 
            nonlocal x_parent
            nonlocal y_parent 
            depth += 1   
               
            if node.val == v:
                if x_or_y == 'x':
                    x_depth = depth
                    x_parent = previous_node_val
                else:
                    y_depth = depth
                    y_parent = previous_node_val
                print("x,y:{0},{1}".format(x_depth, y_depth))    
                
            if node.left != None:
                previous_node_val = node.val
                inorder(node.left, v, depth, x_or_y)
            if node.right != None:
                previous_node_val = node.val
                inorder(node.right, v, depth, x_or_y)
        

        inorder(root, x, 0, 'x')
        inorder(root, y, 0, 'y')
        
        print("x_parent, y_parent: {0},{1}".format(x_parent, y_parent))
        return x_depth == y_depth and x_parent != y_parent

    
    
    
    
    
    
    
    




