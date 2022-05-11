from typing import List 
'''
1118 ~ 1121 

너무 쉬운 문제 
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = sorted(list(s), reverse = True)

        if len(l) < 3:
            return l[0]
        else:
            return l[2]


