'''
0744 

이거 은근 어려운디...? 뭐지? 
binary tree의 특성을 이용했다고 한다. 그런데 어떤 특성을 이용했는지? 
일단 답은 맞았는데 애매한데 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def sortToBST(nums):
            if len(nums) == 0:
                return None
            mid = nums[len(nums) // 2]
            root = TreeNode(mid)
            root.left = sortToBST(nums[:len(nums) // 2])
            root.right = sortToBST(nums[len(nums) // 2 + 1:])
            return root 
        
        
        return sortToBST(nums)

