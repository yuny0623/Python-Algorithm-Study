'''
0839 ~ 0842 
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        po = 1
        while po < n:
            po = po*3
        if po == n:
            return True
        else:
            return False 
        