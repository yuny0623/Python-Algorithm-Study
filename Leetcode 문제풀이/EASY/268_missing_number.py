from typing import List 
'''
0115 ~ 0120  

너무 느린데 3000ms
'''
# 1번 솔루션
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort() 
        for i in range(l + 1):
            if i not in nums:
                return i

'''
좀더 빠르게? 308 ms
'''
# 2번 솔루션 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort() 
        i = 0
        for n in nums:
            if i != n:
                return i
            i += 1
        return i 

'''
더 빠르게? 148ms
속도 줄이긴 했는데 로직이 더러워졌다. 
'''
# 3번 솔루션 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() 
        
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1
        if nums[0] == 1:
            return 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1 :
                return nums[i - 1] + 1
    
        return nums[-1] + 1






