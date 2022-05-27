'''
1119 ~ 1126 

Runtime: 48 ms, faster than 37.10% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 13.9 MB, less than 18.51% of Python3 online submissions for Uncommon Words from Two Sentences.

코멘트:
히든케이스같은거 없는 문제임. 
참고로 split 은 문자열 split 하면 리스트를 반환해줌.
이걸 활용하면됨. 
생각보다 코드가 좀 길어졌다. 
'''
from collections import defaultdict 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d1 = defaultdict(int)
        for w in s1.split():
            d1[w] += 1
        d2 = defaultdict(int)
        for w in s2.split():
            d2[w] += 1
        
        candidate1 = []
        candidate2 = []
        for key, value in d1.items():
            if value == 1:
                candidate1.append(key)
        for key, value in d2.items():
            if value == 1:
                candidate2.append(key)
                
        result = []
        for c in candidate1:
            if c not in s2.split():
                result.append(c)
        for c in candidate2:
            if c not in s1.split():
                result.append(c)
        return result 
        