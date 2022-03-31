from typing import List
'''
1145 ~ 1152  
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        for n in s:
            if nums.count(n) > (len(nums) // 2):
                return n 

'''
성능개선 
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]
        for i in range(1,len(nums)):
            if count == 0 :
                major = nums[i]
                count = 1
            elif nums[i] == major : 
                count += 1
            else : 
                count -= 1
        return major