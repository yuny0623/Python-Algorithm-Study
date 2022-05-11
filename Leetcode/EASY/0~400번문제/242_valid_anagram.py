'''
1108 ~ 1111 
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li1 = [0] * 123 
        li2 = [0] * 123
        for c in s:
            li1[ord(c)] += 1
        for c in t:
            li2[ord(c)] += 1
            
        if li1 == li2:
            return True
        else:
            return False 
        
        
            