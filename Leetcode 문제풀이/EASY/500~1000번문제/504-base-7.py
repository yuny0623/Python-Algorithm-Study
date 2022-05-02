'''
0420 ~ 0439 
Runtime: 61 ms, faster than 8.31% of Python3 online submissions for Base 7.
Memory Usage: 13.8 MB, less than 63.57% of Python3 online submissions for Base 7.

생각보다 예외조건이 까다로운 문제인듯 
왜 계속 틀렸을까? 음수를 divmod 의 인자로 주면 오답이 나옴. 
양수라고 가정하고 풀고 마지막에 음수 기호를 붙여주는게 나음. 
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = [] 
        if num == 0:
            return '0'

        if num < 7 and num > -7:
            return str(num)

        positive = True 
        if num<0:
            positive = False 
            num = -num 
        a = 8
        b = 8 
        while a >= 7:
            a, b = divmod(num, 7)
            num = a 
            result.append(str(b))
        result.append(str(a))
        
        if not positive:
            result.append('-')
        return ''.join(result[::-1])

        