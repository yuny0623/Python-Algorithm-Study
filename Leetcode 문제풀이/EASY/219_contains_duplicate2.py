from typing import List 
'''
0947 ~ 1038 
어렵네요 이거 ㄷㄷ 

https://leetcode.com/problems/contains-duplicate-ii/
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic : 
                if abs(i - dic[nums[i]]) <=k :
                    return True
                else :
                    dic[nums[i]] = i 
            else:
                dic[nums[i]] = i
        return False