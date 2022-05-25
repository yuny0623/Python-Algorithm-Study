'''
0754 ~ 8000 
Runtime: 1041 ms, faster than 85.38% of Python3 online submissions for Monotonic Array.
Memory Usage: 28 MB, less than 84.56% of Python3 online submissions for Monotonic Array.

코멘트: 
쉬운문제. 근데 1초가 걸리는데 sorted 안쓰고는 못할까용 
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums, reverse=True) == nums or sorted(nums) == nums

'''
새로운 솔루션:
속도차이없음
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        reverse_flag = False 
        if max(nums) == nums[0]:
            reverse_flag = True
        return sorted(nums, reverse=reverse_flag) == nums 