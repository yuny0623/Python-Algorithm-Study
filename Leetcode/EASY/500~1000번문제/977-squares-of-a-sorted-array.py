'''
1146 ~ 1151
Runtime: 317 ms, faster than 50.08% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 50.09% of Python3 online submissions for Squares of a Sorted Array. 
코멘트: 
lambda 쓰면 쉬워용. 
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, nums))