'''
0309 ~ 0354 <답지 보고 풀음>

코멘트: 
경우의 수를 많이 생각해봐야 하는 문제. 
1. 음수* 음수* 정수 <- 가장 클 가능성이 있는 후보군 
2. 정수* 정수* 정수 <- 가장 클 가능성이 있는 후보군 
3. 음수* 음수* 음수 <- 아마 가장 작은 경우 
위 세개의 경우를 max 로 넘기면 답이 나온다. 

Runtime: 418 ms, faster than 22.10% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 15.2 MB, less than 69.11% of Python3 online submissions for Maximum Product of Three Numbers.
'''

from collections import defaultdict 
class Solution: 
    def maximumProduct(self, nums: List[int]) -> int:
        product = 1
        if len(nums) <= 3:         
            for n in nums:
                product *= n
            return product 
        
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[2], nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])

            
        
        