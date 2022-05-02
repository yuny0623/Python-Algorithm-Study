'''
0845 ~ 0948 

이전에 풀었던 문제랑 아주 유사함. 
isporphic strings 문제랑 거의 똑같음. -> 그냥 똑같음. 
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li_p = list(pattern)
        li_w = s.split(" ")
        
        if len(li_p) != len(li_w):
            return False 
        
        mapPW, mapWP = {}, {}
        for p, w in zip(li_p, li_w):
            if ((p in mapPW and mapPW[p] != w) or
                (w in mapWP and mapWP[w] != p)):
                return False
            mapPW[p] = w
            mapWP[w] = p
        return True