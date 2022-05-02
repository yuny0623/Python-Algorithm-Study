'''
1151  ~ 1252 
생각했던 것보다 오래 걸린 문제. 
어렵네요 뭐징 

positive integer 라고 했으니 n으로 음수가 들어오면 곧바로 False 를 리턴한다. 
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False 
        if n < 0:
            return False 
        while n%2 == 0:
            n = n//2
        if n == 1:
            return True
        while n%3 == 0:
            n = n//3
        if n == 1:
            return True
        while n%5 == 0:
            n = n//5
        if n == 1:
            return True
        return False 

'''
좀더 깔끔하게 짜볼순 없을까. 
'''

class Solution:
    def isUgly(self, n:int) -> bool:
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n = n//p
        return n == 1
