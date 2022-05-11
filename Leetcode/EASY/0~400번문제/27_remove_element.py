class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        change_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[change_index] = nums[i]
                change_index += 1
        return change_index 
        