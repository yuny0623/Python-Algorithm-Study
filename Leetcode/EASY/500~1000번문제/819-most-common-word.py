'''
0910 ~ <답지 보고 풀음>

코멘트: 
정규표현식 써서 푸신 문들이 많다. 문제 시작 전에 제대로 풀기 위해 
일종의 처리를 거쳐야하는데 그 부분에서 조금 신경쓰이는 부분이 있음. 

'''
from collections import defaultdict 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if len(paragraph) < 0:
            return [] 
        str_li = []
        word = [] 
        for c in paragraph:
            if c not in "!?',;. ":
                word.append(c)
            else:
                str_li.append(''.join(word).lower())
                word = []
        print(str_li)
    
        d = defaultdict(int)
        for s in str_li:
            if s not in banned:
                d[s] += 1
        print(d)
        d = sorted(d.items(), reverse=True,key = operator.itemgetter(1))
        return d[0][0]
            
                