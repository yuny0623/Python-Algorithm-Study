'''
0511 
~ 0514 
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    continue
                else:
                    return i 
            return len(nums)
