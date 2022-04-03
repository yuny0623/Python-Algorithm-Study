'''
1116 ~ 1201 
1번 솔루션 101 ms 

쉬운문제임. 
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        li_n = list(ransomNote)
        li_m = list(magazine)
        
        ch = [0] * (122 + 1)
        for c in magazine:
            ch[ord(c)] += 1
        
        for c in ransomNote: 
            ch[ord(c)] -= 1
            if ch[ord(c)] == -1:
                return False
        return True 

''' 
메모리 절약 가능? 
2번 솔루션 
14.4mb
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ch = [0] * 26
        for c in magazine:
            ch[ord(c) - 97] += 1
        
        for c in ransomNote: 
            ch[ord(c) - 97] -= 1
            if ch[ord(c) - 97] == -1:
                return False
        return True 
            