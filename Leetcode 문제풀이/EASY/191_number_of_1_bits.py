'''
1218 ~ 1222 
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n))[2:].count('1')
       
        
