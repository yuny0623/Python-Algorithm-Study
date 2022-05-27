'''
0152 ~ 0209 

Runtime: 62 ms, faster than 12.83% of Python3 online submissions for Number of Lines To Write String.
Memory Usage: 13.9 MB, less than 69.34% of Python3 online submissions for Number of Lines To Write String.

코멘트: 
첫번째 줄부터 쓰는 것이기 때문에 변수 line을 1로 초기화해야하는 것에 주의 
'''
from collections import defaultdict 
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1 # 첫째줄부터 시작이니까 1로 초기화
        
        d = defaultdict(int)
        for i in range(len(widths)):
            d[chr(97 + i)] = widths[i]
        
        sums = 0
        for c in s:
            if sums + d[c] <= 100:
                sums += d[c]
            elif sums + d[c] > 100:
                sums = d[c]
                line += 1
                
        return [line, sums]
            