'''
1009  ~ 1013 

Runtime: 37 ms, faster than 72.36% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 13.8 MB, less than 58.52% of Python3 online submissions for N-th Tribonacci Number.

코멘트 :
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0] * (37 + 1)
        d[0] = 0
        d[1] = 1
        d[2] = 1 
        for i in range(3, n + 1):
            d[i] = d[i -3] + d[i - 2] + d[i - 1] 
        return d[n]