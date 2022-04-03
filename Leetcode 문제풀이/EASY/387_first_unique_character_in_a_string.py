'''
1204 ~ 1207 

1번 솔루션 8236ms 
'''
# 1번 솔루션 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1 

'''
1번 너무 느림. 속도 높이기 가능? 

2번 솔루션 - 100ms 
collections 모듈 사용으로 속도 줄일 수 있었음. 
'''    
# 2번 솔루션 
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        s = list(s)
        cnt_dict = Counter(s)
        i = 0

        for word in s:
            if cnt_dict[word] == 1:
                answer = i
                break
            i = i + 1

        return answer



