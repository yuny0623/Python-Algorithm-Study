'''
0910 ~ <답지 보고 풀음>

Runtime: 56 ms, faster than 36.26% of Python3 online submissions for Most Common Word.
Memory Usage: 14.1 MB, less than 6.22% of Python3 online submissions for Most Common Word.

코멘트: 
정규표현식 써서 푸신 문들이 많다. 문제 시작 전에 제대로 풀기 위해 
일종의 처리를 거쳐야하는데 그 부분에서 조금 신경쓰이는 부분이 있음. 

이거 정규표현식 안쓰면 못푸는건가? 
'''
import re
from collections import defaultdict 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        d = defaultdict(int)
        for w in para:
            d[w] += 1
        
        return max(d.keys(), key = lambda k: d[k])
                