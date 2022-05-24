'''
1006 ~ 1023 
Runtime: 90 ms, faster than 31.25% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.2 MB, less than 17.42% of Python3 online submissions for Shortest Distance to a Character.

코멘트:
좋은 문제임. 
오른쪽 왼쪽으로 나눠서 find 하는 방식으로 접근하면 쉽게 풀 수 있음. 
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        if len(s) == 1:
            return [0]
        answer = [] 
        for i in range(len(s)):
            left = s[:i].rfind(c)
            right = s[i:].find(c)
            print(left, right)
            if left != -1 and right != -1:
                answer.append(min(abs(i - left) , right))
            else:
                answer.append(abs(i-left)) if left != -1 else answer.append(right)
        print(answer)
        return answer 


