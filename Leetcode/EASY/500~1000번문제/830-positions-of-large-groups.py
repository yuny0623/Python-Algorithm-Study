'''
0948 ~ 0959 

Runtime: 58 ms, faster than 36.66% of Python3 online submissions for Positions of Large Groups.
Memory Usage: 13.9 MB, less than 27.81% of Python3 online submissions for Positions of Large Groups.

코멘트: 
좋은 문제임. 
투 포인터처럼 전진하면서 푸는게 제일 쉬움. 
'''

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        interval = [] 
        start = 0
        end = 0 
        while end < len(s):
            if s[start] == s[end]:
                end += 1
            else:
                interval.append([start, end-1])
                start = end
        interval.append([start,len(s)-1])
        
        large = []
        for start , end in interval:
            if end - start + 1 >= 3:
                large.append([start,end])
        large = sorted(large, key = lambda x: x[0])
        return large 


