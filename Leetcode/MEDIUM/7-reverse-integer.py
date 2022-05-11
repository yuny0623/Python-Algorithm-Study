'''
0446 ~ 0452 

Runtime: 40 ms, faster than 64.72% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.8 MB, less than 65.59% of Python3 online submissions for Reverse Integer.

딱히 어렵진 않은 문제, 다만 범위 체크해야하는 걸 고려해야함. 
파이썬에 ternary 가 없어서 좀 지저분해보이긴하네. 
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            return 0 if int(str(x)[::-1]) > pow(2, 31) - 1 else int(str(x)[::-1])
        if x < 0:
            return 0 if int('-'+str(-x)[::-1]) < -pow(2, 31) else int('-'+str(-x)[::-1])
        else:
            return 0 