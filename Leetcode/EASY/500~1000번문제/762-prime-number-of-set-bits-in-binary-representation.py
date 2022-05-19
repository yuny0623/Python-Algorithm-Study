'''
0755 ~ 0803 

Runtime: 1145 ms, faster than 24.36% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
Memory Usage: 13.9 MB, less than 76.20% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.

코멘트:
두 문제가 섞인 문제다. 쉬운 문제임. 다만 문제 오해하고 풀 여지있음.
속도가 1초나 걸리는데 좀 더 빠르게 바꿀 순 없을까? 
'''
import math 
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def isprime(x):
            if x == 1:
                return False 
            for i in range(2, int(math.sqrt(x)) + 1):
                if x%i == 0:
                    return False
            return True
        
        prime_number_of_set_bits = 0 
        for i in range(left, right + 1):
            count = bin(i)[2:].count('1')
            print(bin(i)[2:], count)
            if isprime(count):
                prime_number_of_set_bits += 1
                
        return prime_number_of_set_bits
        

'''
개선한 솔루션:
Runtime: 403 ms, faster than 60.89% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
Memory Usage: 14 MB, less than 28.97% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.

속도 많이 줄였다. 위에서 함수 호출 제거해줬음. 
'''

import math 
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_number_of_set_bits = 0 
        
        for i in range(left, right + 1):
            prime = True 
            count = bin(i)[2:].count('1')
            
            if count == 1:
                continue 
                
            for i in range(2, int(math.sqrt(count)) + 1):
                if count%i == 0:
                    prime = False
                    break
                    
            if prime:
                prime_number_of_set_bits += 1
                
        return prime_number_of_set_bits
        