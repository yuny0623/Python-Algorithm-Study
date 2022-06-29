'''
0413 ~ 0415 

Runtime: 1092 ms, faster than 15.62% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 24 MB, less than 68.41% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

코멘트: 
딱히 어렵진 않음. 다만 함수 내에서 리턴할때 리턴 처리를 따로 해주지 않는 실수를 한다면
리턴으로 전달하는 값이 그냥 재귀 도중 사라짐. 즉 caller 스택으로 넘어가면서 해당 stack이 
사라지면 그냥 값도 사라짐. 즉 결과값이 당연히 None -> null 이 나옴. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 0413 ~ 0415 
        # 그냥 리턴하지말고 변수에 할당해서 리턴하는게 나음. 그냥 리턴하면 재귀나오면서 값 없어짐.
        result = None
        def preorder(node):
            nonlocal result 
            if node!= None and node.val == target.val:
                result = node 
                return 
            
            if node.left != None:
                preorder(node.left)
            if node.right != None:
                preorder(node.right)
                
                
        preorder(cloned)
        return result 

''' 
Runtime: 906 ms, faster than 38.63% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 23.9 MB, less than 68.41% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

개선한 솔루션: 
그렇다면 여기서 nonlocal 을 통해서 메모리내에서 외부 var에 접근하기 위해 
메모리 상에서 jump 하지 않고 즉 flow 를 거스르지 않고 가까운 메모리에 접근하게 만들 수 있다면? 
재귀에서 빠져나오면서 자연스럽게 값을 리턴받을 수 있는 방법은 ? -> 아래 솔루션처럼 사용하면됨.
외부에있는 variale 사용하지 않고 내부 variable 쓰면서 그 value 를 리턴하면 
굳이 jump 많이 하지 않아도 되서,  메모리 jump 줄일 수 있다는 점에서 더 나음. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def preorder(node):
            result = None
            if node!= None and node.val == target.val:
                result = node
                return result 
            
            if node.left != None:
                result = preorder(node.left)
                if result:
                    return result 
            if node.right != None:
                result = preorder(node.right)
                if result:
                    return result 
                
            return result 
                
                
        return preorder(cloned)