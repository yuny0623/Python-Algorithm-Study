from typing import List 
'''
0223 ~ ? 0840 

정렬문제네. 

버블정렬인가? 
어렵네 뭐지. 

생각보다 어렵게 푼 문제다. 
문제 조건이 추가적으로 메모리 쓰지말고 in-place조건하에
진행하라고 해서 접근을 잘못했다. 

1번 솔루션은 172ms 나왔다. 2번 솔루션 참고해라. 더 깔끔함. 
'''
# 1번 솔루션 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0 
        right = 0
        
        while right < len(nums):
            if nums[right] == 0:
                right += 1
                continue 
            elif nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
                
        return nums 
    
'''
좀더 이쁘게 풀 순 없을까? 333ms 
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums 
        
        
            
        
            
                
        
            
        
            
        

