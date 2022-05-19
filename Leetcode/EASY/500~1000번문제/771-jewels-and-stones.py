'''
0839 ~ 0841 
Runtime: 39 ms, faster than 62.19% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.8 MB, less than 59.23% of Python3 online submissions for Jewels and Stones.

코멘트: 
파이썬에서는 쉬운 문제 
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            if j in stones:
                count += stones.count(j)
        return count 

