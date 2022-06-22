'''
0224 ~ <답지보고 풀음 >

Runtime: 66 ms, faster than 8.27% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 13.8 MB, less than 55.94% of Python3 online submissions for Split a String in Balanced Strings.

코멘트: 이건 내가 문제를 잘못 읽었다. 
그리고 아래 코드처럼 count 변수를 가지고 비교하면서 ++, -- 해주는 동작은 앞으로 
쓸일이 많을것같으니 이 방식은 기억해두자. 
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0 
        balancedCount = 0
        for i in range(len(s)):
            if s[i] == 'R':
                count += 1
            if s[i] == 'L':
                count -= 1
            if count == 0:
                balancedCount += 1
        
        return balancedCount




