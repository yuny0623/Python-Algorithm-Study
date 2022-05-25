'''
1137 ~ 1140 
Runtime: 59 ms, faster than 15.65% of Python3 online submissions for Backspace String Compare.
Memory Usage: 14 MB, less than 23.29% of Python3 online submissions for Backspace String Compare.

코멘트:
문제 자체는 그냥 구현으로 풀면 쉬운 문제
근데 효율성 문제인것 같음. 리스트에서 넣고 빼기만 하면 되는 문제인데
리스트에 넣고 빼는 연산자체를 없애고 다른 방법쓰면 좀더 빠르게 할 수 있을지도 
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = []
        for i in range(len(s)):
            if s[i] != '#':
                result_s.append(s[i])
            else:
                if len(result_s) >0:
                    result_s.pop()
        result_t = []
        for i in range(len(t)):
            if t[i] != '#':
                result_t.append(t[i])
            else:
                if len(result_t) >0:
                    result_t.pop()
        
        print(result_s)
        print(result_t)
        return result_s == result_t


