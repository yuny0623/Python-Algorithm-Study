'''
이거 시간 초과 나오네 ㄷㄷ 
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
        return max(nums)
            
            
            
            