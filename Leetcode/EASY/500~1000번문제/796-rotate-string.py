'''
0916 ~ 0918 

Runtime: 44 ms, faster than 41.62% of Python3 online submissions for Rotate String.
Memory Usage: 13.9 MB, less than 14.94% of Python3 online submissions for Rotate String.

코멘트: 
굳이 rotate 해가면서 풀 필요없다. 
leftmost 를 rightmost 로 이동시키는 규칙으로만 움직여야한다면
s + s 에서 goal 이 있는지만 보면 된다. 
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) > len(goal):
            return False 
        if goal in (s + s):
            return True
        return False 