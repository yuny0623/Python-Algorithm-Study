'''
0426 ~ 0440 
재밌는 문제
쉬움. 
'''
class Solution:
    def findComplement(self, num: int) -> int:
        s = str(bin(num)[2:])
        print("s:{0}".format(s))
        print(type(s))
        result = []
        for c in s:
            if c == '0':
                result.append('1')
            elif c == '1':
                result.append('0')
        print(result)
        return int(''.join(result), base=2)
        
