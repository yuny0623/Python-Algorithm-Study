from typing import List 
'''
1005 ~ 1032 

답지 보고 풀음. 피곤해서 쉬운건데 못풀었네. 걍잡시다. 아프다... 
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        end = len(nums)
        result = set(list(range(1, end + 1))) - set(nums)
        return result 
