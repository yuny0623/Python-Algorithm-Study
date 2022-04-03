'''
0128 ~ 0128  

간단함. 
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        li_s = [0] * 26

        s_l = list(s)
        t_l = list(t)
        for i in range(len(s_l)):
            li_s[ord(s_l[i]) - 97] += 1
        for i in range(len(t_l)):
            li_s[ord(t_l[i]) - 97] -= 1

        for i in range(len(li_s)):
            if li_s[i] == -1:
                return chr(i + 97)
        
            
        
            


