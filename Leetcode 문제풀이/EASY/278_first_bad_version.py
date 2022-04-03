'''
0133 ~ 0203 
이분 탐색 떠올리면 다 푼거 
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start = 0
        end = n 
        mid = 0 
        while start <= end:
            mid = (start + end) // 2 
            if isBadVersion(mid) == True:
                end = mid - 1
            if isBadVersion(mid) == False:
                start = mid + 1
            
        return start 


