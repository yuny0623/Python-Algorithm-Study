'''
0842 ~ 0846 

Runtime: 44 ms, faster than 49.58% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14 MB, less than 7.38% of Python3 online submissions for Minimum Distance Between BST Nodes.

코멘트: 
쉬운문제다. BST를 inorder 로 돌면 저절로 정렬되서 나온다는걸 알고 있으면
나중에 sort 하는 번거로운 동작이 필요없다. 그런데 최소 차이를 구하는 과정이 
for 문 말고 좀더 괜찮은 방법이 있을 것 같은데... inorder 돌면서 아예 거기서 
구해버리는 방법은 없을까? 개선해보기 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        def inorder(node):
            if node.left != None:
                inorder(node.left)
            result.append(node.val)
            if node.right != None:
                inorder(node.right)
        inorder(root)
        
        min_diff = sys.maxsize 
        for i in range(1, len(result)):
            if abs(result[i] - result[i - 1]) < min_diff:
                min_diff = abs(result[i] - result[i - 1])
        return min_diff 

'''
Runtime: 37 ms, faster than 71.90% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14.2 MB, less than 7.38% of Python3 online submissions for Minimum Distance Between BST Nodes.

개선한 솔루션: 
나머지 솔루션보다 70퍼센트 빠르다. 속도도 7ms 줄였음. 그리고 추가적인 반복문없음. 
근데 사실 직관성은 위 코드가 더 나은듯 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = sys.maxsize 
        previous = 100002
        
        def inorder(node):
            nonlocal previous
            nonlocal min_diff 
            
            if node.left != None:
                inorder(node.left)
                
            if abs(previous - node.val) < min_diff:
                min_diff = abs(previous - node.val)
            previous = node.val 

            if node.right != None:
                inorder(node.right)
                
        inorder(root)
        
        return min_diff 