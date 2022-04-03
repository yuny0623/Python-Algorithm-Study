'''
1105 ~ 1107  
쉬움. 

1번 솔루션 42ms 
''' 

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        for i in range(int(math.sqrt(num)) + 1):
            if i*i == num:
                return True
        return False 

'''
위 방식말고 다른 방법 없나. 
2번 솔루션 38 ms 
이것보다 좀더 빠른거 없나? 
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        k = 1
        square = 1 
        while square < num:
            square = k * k
            k += 1
        if square == num:
            return True
        return False 


'''
3번 솔루션 
'''