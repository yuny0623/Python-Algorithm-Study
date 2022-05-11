'''
1051 ~ 1114 

신박한 문제네 
이런 유형은 처음봄. 그냥 구현문제인듯. 
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        k = -1
        while n > 0:
            n -= i
            i += 1
            k += 1
        if n == 0:
            return k + 1
        return k
        
            
            



