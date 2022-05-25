'''
0632 ~ <회의하고옴ㅋ> ~ 0741 

Runtime: 52 ms, faster than 6.64% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 14 MB, less than 39.48% of Python3 online submissions for Increasing Order Search Tree.

코멘트: 
이 문제는 문제가 2개로 나뉘어있다. 먼저 앞의 문제는 순회해서 일렬로 세우는 구현문제. 
그리고 두번째는 순회한 일렬 결과 리스트를 TreeNode 로 이어붙이는 문제다. 
예외 까다로운거 없음.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def postorder(node):
            if node.left != None:
                postorder(node.left)
            nodes.append(node.val)
            if node.right != None:
                postorder(node.right)

        postorder(root)
        print(nodes)
        
        if len(nodes) == 1:
            return TreeNode(nodes[0], None, None)
        
        new_root = TreeNode(nodes[0], None, None)
        start = new_root   
        for i in range(1, len(nodes)):
            new_root.right = TreeNode(nodes[i], None, None)
            new_root = new_root.right
        
        return start 
            