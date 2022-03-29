class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(set(nums))
        temp.sort()
        for i, v in enumerate(temp):
            nums[i] = v
        
        return len(temp)
            
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0 
        change_index = 1
        for i in range(len(nums)):
            if i != 0 and nums[i - 1] != nums[i]:
                nums[change_index] = nums[i]
                change_index +=1 
        return change_index 