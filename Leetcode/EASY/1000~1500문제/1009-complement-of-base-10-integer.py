'''
0711 ~ 0716 
Runtime: 38 ms, faster than 68.30% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 13.9 MB, less than 51.80% of Python3 online submissions for Complement of Base 10 Integer.

코멘트: 
문제 자체는 쉬움. 
이것보다 쉽게 푸는방법이 분명 있을 것.
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        result = []
        for n in bin(n)[2:]:
            if n == '1':
                result.append('0')
            else:
                result.append('1')
        return int(''.join(result), 2)
                