'''
0446 ~ 0457 

Runtime: 39 ms, faster than 77.09% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 56.08% of Python3 online submissions for Excel Sheet Column Number.

코멘트: 
어렵다고 생각하고 풀었는데 막상 풀고 나니 어렵진 않았음. 
구현하기만 하면 되는 문제인데 정확한 범위 + 자릿수가 정확해야해서 
조금 생각하고 풀어야할 문제임. 
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = [chr(i) for i in range(65, 65 + 26)]
        col = 0
        times = 1
        for i in range(len(columnTitle) - 1, -1, -1): 
            col += times * (alpha.index(columnTitle[i]) + 1)
            times *= 26 
        return col 




