'''
1144 ~ 1149 
Runtime: 121 ms, faster than 29.63% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.3 MB, less than 59.49% of Python3 online submissions for Peak Index in a Mountain Array.

코멘트: 
쉬운 문제. 구현만 하면 됨. 
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = 0 
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                peak = i - 1
                return peak 
