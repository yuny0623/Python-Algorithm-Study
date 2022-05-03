'''
0334 ~ 0342 

Runtime: 6588 ms, faster than 5.19% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16.2 MB, less than 31.54% of Python3 online submissions for Minimum Absolute Difference in BST.

일단 시간이 6초 걸리는게 너무 느림. 속도 줄여보자. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        li = []
        diff = 100001 
        def preorder(node):
            nonlocal diff
            nonlocal li 
            if len(li) > 0:
                for n in li:
                    if abs(n - node.val) < diff:
                        diff = abs(n - node.val)
            li.append(node.val)
            
            if node.left != None:
                preorder(node.left)
            if node.right != None:
                preorder(node.right)
                
        preorder(root)
        
        return diff 

'''
개선한 솔루션1: 

Runtime: 129 ms, faster than 5.52% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16.4 MB, less than 7.72% of Python3 online submissions for Minimum Absolute Difference in BST.

런타임은확실히 많이줄였음. 아마 재귀내에 리스트 append 가 없어서 많이 줄어든듯. 
근데 faster than 이 너무 낮음. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        result = [] 
        def inorder(node):
            nonlocal result
            if node.val == None:
                return 
            if node.left != None:
                inorder(node.left)
            result.append(node.val)
            if node.right != None:
                inorder(node.right)
        
        inorder(root)
        print(result)
        diff = 100001 
        prev = result[0]
        for i in range(1, len(result)): 
            diff = min(abs(result[i] - prev), diff)
            prev = result[i]
            
        return diff 
        
            
'''
개선한 솔루션3: 
Runtime: 65 ms, faster than 66.73% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16 MB, less than 81.30% of Python3 online submissions for Minimum Absolute Difference in BST.

속도 두배 줄이고 faster than 많이 올렸다. 이미 inorder 로 돌았으니까 어차피 정렬되있음. 그러니까
diff 계산할때 min 에서 굳이 abs 로 절대값 구해줄 필요없지. 어차피 큰거에서 작은거 빼니까요. 
그리고 nonlocal 로 중첩된 재귀 내에서 외부로 계속 참조하지 말고 그냥 내부에 매개변수로 전달해주면서
사용하는게 조금더 나을것 같아서 바꾼 코드. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = [] 
        def inorder(node, li):
            if node.left != None:
                inorder(node.left, li)
            li.append(node.val)
            if node.right != None:
                inorder(node.right, li)
        
        inorder(root, result)
        
        diff = 100001 
        prev = result[0]
        for i in range(1, len(result)): 
            diff = min(result[i] - prev, diff)
            prev = result[i]
            
        return diff 
        
            
            
            
            
            
                  
            
            
