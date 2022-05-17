'''
0835 ~ 0838

Runtime: 39 ms, faster than 76.28% of Python3 online submissions for Largest Number At Least Twice of Others.
Memory Usage: 13.9 MB, less than 59.52% of Python3 online submissions for Largest Number At Least Twice of Others.

코멘트:
어렵지 않은 문제. 
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx = nums.index(max(nums))
        for i in range(len(nums)):
            if i != idx:
                if nums[i]*2 <= nums[idx]:
                    continue
                else:
                    return -1 
        return idx 

