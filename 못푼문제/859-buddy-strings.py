'''
1150 ~ <답지 보고 풀음.>

Runtime: 37 ms, faster than 78.87% of Python3 online submissions for Buddy Strings.
Memory Usage: 14.2 MB, less than 61.80% of Python3 online submissions for Buddy Strings.

코멘트:
생각보다 예외 케이스가 많음. 
예외만 주의하면 쉽게 풀 수 있음. 
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        
        if s == goal:
            if len(set(s)) < len(s):
                return True
            else:
                return False 
        
        s = s[:]
        goal = goal[:]
        diff = []
        i = 0
        for a, b in zip(s, goal):
            if a != b:
                diff.append(i)
            i += 1
            
        if len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
        return False 