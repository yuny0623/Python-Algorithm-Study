'''
0659 ~ 0715 

Runtime: 437 ms, faster than 5.12% of Python3 online submissions for Perfect Number.
Memory Usage: 14.3 MB, less than 12.98% of Python3 online submissions for Perfect Number.

솔루션1: 
400ms 면 좀 많이 느리다. 개선할 수 있는지? 
'''
import math 

class Solution:
    def checkPerfectNumber(self, num: int) -> bool: 
        if num <= 2:
            return False 
        divisor = [1] 
        for i in range(2, int(math.sqrt(num)) + 1):
            print(divisor)
            if num%i == 0:
                divisor.append(i)
                divisor.append(num//i)
        
        if sum(divisor) == num:
            return True
        return False 

'''
개선한 솔루션2: 
Runtime: 49 ms, faster than 59.88% of Python3 online submissions for Perfect Number.
Memory Usage: 13.8 MB, less than 59.17% of Python3 online submissions for Perfect Number.

원래 리스트로 연산하던걸 그냥 total 로 합 구하는 방법으로 바꿨지. 
살짝 빨라졌지. 근데 아직도 개선할 수 있는 부분이 있나? 
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool: 
        if num <= 2:
            return False 
        total = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0:
                total += i 
                total += num//i
        
        if total == num:
            return True
        return False 

'''
개선한 솔루션3:
Runtime: 38 ms, faster than 84.76% of Python3 online submissions for Perfect Number.
Memory Usage: 14 MB, less than 12.98% of Python3 online submissions for Perfect Number.

for 루프에서 total 계산하는 부분을 한번에 계산해주는 코드로 바꿨지. 
살짝 성능 개선됨. 
'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool: 
        if num <= 2:
            return False 
        total = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0:
                total = total + i + num//i 
        
        if total == num:
            return True
        return False 