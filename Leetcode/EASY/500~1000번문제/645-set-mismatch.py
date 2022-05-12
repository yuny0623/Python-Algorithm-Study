'''
0840 ~ 0905 

Runtime: 253 ms, faster than 61.17% of Python3 online submissions for Set Mismatch.
Memory Usage: 16.4 MB, less than 9.89% of Python3 online submissions for Set Mismatch.

코멘트:
굳이 defaultdict 를 써야할까? 조금 간단한 문제인데 모듈까지 써가면서 풀어야하나? 없애보자. 
'''
from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        high = len(nums) # 2 
        miss = list(set([x for x in range(1, high + 1)]) - set(nums))[0] # 1 2 - 1 -> 2 
        dup = 0
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for key,value in d.items():
            if value >= 2:
                dup = key 
        return [dup, miss]
        
        # 2 3 3 4 5 6 
    
'''
두번째 솔루션:
이건 defaultdict 안써도 된다. 

Runtime: 262 ms, faster than 57.12% of Python3 online submissions for Set Mismatch.
Memory Usage: 16.6 MB, less than 6.73% of Python3 online submissions for Set Mismatch.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        high = len(nums) # 2 
        miss = list(set([x for x in range(1, high + 1)]) - set(nums))[0] # 1 2 - 1 -> 2 
        dup = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
                break
        return [dup, miss]
        
        # 2 3 3 4 5 6 

'''
정리
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        high = len(nums) # 2 
        miss = list(set([x for x in range(1, high + 1)]) - set(nums))[0] 
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
                return [dup, miss]            
                