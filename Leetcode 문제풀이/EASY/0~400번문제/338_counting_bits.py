'''
0842  ~ 0928 
그냥 비트 세주면 된다. 
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(list(str(bin(i))).count('1'))
        return result 