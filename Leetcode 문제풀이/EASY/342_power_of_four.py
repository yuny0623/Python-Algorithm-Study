'''
0929 ~ 0931 
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        po = 1
        while po < n:
            po = po*4
        if po == n:
            return True
        else:
            return False 