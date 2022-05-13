'''
0401 ~ 0406 

Runtime: 38 ms, faster than 58.95% of Python3 online submissions for Binary Number with Alternating Bits.
Memory Usage: 13.8 MB, less than 95.92% of Python3 online submissions for Binary Number with Alternating Bits.

코멘트:
단순 구현 문제임. 
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = list(map(int, bin(n)[2:]))
        for i in range(1, len(b)):
            if b[i - 1] == b[i]:
                return False
        return True 
            