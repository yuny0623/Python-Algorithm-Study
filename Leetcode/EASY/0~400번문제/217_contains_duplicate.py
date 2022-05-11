from typing import List 
'''
0908 ~ 0933 

성능개선 필요함. 
딱봐도 느리네. 8퍼센트 성능 
'''
# 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:     
        a = sorted(list(set(nums))) # 1 2 3 
        b = sorted(nums)   # 1 1 2 3 
        if a == b:
            return False
        return True

'''
성능개선한 코드 <- 내가 작성함. <- 91 퍼센트 성능 
근데 너무 날먹인데 다른 방법 없을까용... 
'''
# 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:     
        if len(set(nums)) != len(nums):
            return True
        return False 

'''
정석대로 풀자. <- 5퍼센트... 중간 코드2 내가 작성한게 젤 빠르네용 
'''
# 3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:     
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 

        
        