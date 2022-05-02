'''
1151  ~ 1216 
Reverse bits of a given 32 bits unsigned integer.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[2:][::-1]
        result = ['0'] * 32
        for i in range(len(s)):
            result[i] = s[i]
        
        r = ''.join(result)
        return int('0b' + r, 2)
            

        