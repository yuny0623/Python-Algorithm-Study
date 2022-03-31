'''
0624 ~ 0856 
생각보다 어렵네요 뭐지. 
해쉬맵을 생각못하면 풀기 까다롭네요 
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}    
        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True
    
            