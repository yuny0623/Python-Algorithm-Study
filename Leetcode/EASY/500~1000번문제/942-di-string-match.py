'''
0542 ~ 0556 
Runtime: 92 ms, faster than 50.40% of Python3 online submissions for DI String Match.
Memory Usage: 15.3 MB, less than 44.05% of Python3 online submissions for DI String Match.

코멘트: 
이건 잘 모르겠넹. 
-> 솔루션보고 풀음. permutation 은 그냥 digit String 을 의미한다고 보면 된다. 
문맥에 따라서 다르겠지만 이 경우는 순열조합문제가 아니라 digit string이 있는데
그걸 가지고 문제를 풀어내면됨. -> 그리고 문제 자체가 꽤 직관적이지 않음. 

참고로 
I는 increasing 
D는 Decreasing 이다... 
'''
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # 지문 제대로 읽읍시다. 
        low = 0 
        high = len(s)
        new_s = [] 
        for i in range(len(s)):
            if s[i] == 'I':
                new_s.append(low)
                low += 1
            if s[i] == 'D':
                new_s.append(high)
                high -= 1
            
        new_s.append(low)
        print(new_s)
        return new_s 



