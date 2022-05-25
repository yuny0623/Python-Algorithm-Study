'''
1042 ~ 1135 
Runtime: 100 ms, faster than 5.28% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 13.8 MB, less than 66.64% of Python3 online submissions for Rectangle Overlap.

코멘트: 이건 문제가 뭔지 좀 이해가 안간다. 
지문이 이해가 안된 상태임.
-> 다시 읽어보면 되요 ~ 
''' 
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[2] > rec2[0] and rec1[3] > rec2[1] and rec1[0] < rec2[2] and rec1[1] < rec2[3]
        



