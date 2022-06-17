'''
0711 ~ 0716 
Runtime: 38 ms, faster than 68.30% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 13.9 MB, less than 51.80% of Python3 online submissions for Complement of Base 10 Integer.

코멘트: 
문제 자체는 쉬움. 
이것보다 쉽게 푸는방법이 분명 있을 것. -> 더 줄일 수 있을듯 
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
                
'''
Runtime: 30 ms, faster than 92.01% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 13.8 MB, less than 51.80% of Python3 online submissions for Complement of Base 10 Integer.

두번째 솔루션: 
이건 한줄로 끝낼 수 있다. 
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join(list(map(str, [1 - num for num in list(map(int, str(bin(n)[2:])))]))), 2)
                

