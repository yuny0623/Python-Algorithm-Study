'''
0130 ~ 0136 

쉬움. 
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        s_pos = 0
        for i in range(len(t)):
            if s[s_pos] == t[i]:
                s_pos += 1
            elif s[s_pos] != t[i]:
                continue 
            if s_pos == len(s):
                break 
        
        if s_pos == len(s):
            return True
        else:
            return False 