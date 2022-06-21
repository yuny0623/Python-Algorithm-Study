'''
0153 ~ 2000 

Runtime: 45 ms, faster than 71.60% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14.1 MB, less than 32.81% of Python3 online submissions for Unique Number of Occurrences.

코멘트: 
문제 자체가 뭘 뜻하는지를 알지를 못해서 문제를 풀지를 못했다. 지문을 읽고도 무슨 내용인지 몰랐다. 
근데 그냥 빈도수의 unique 함을 알아낸다는걸로 이해하면 된다. 
'''

from collections import defaultdict 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for a in arr:
            d[a] += 1
        
        v_li = sorted(d.values())
        for i in range(1, len(v_li)):
            if v_li[i - 1] == v_li[i]:
                return False 
        return True 








