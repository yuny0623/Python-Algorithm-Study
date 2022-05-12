'''
0812 ~ 
Runtime: 343 ms, faster than 79.63% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 16.5 MB, less than 6.31% of Python3 online submissions for Longest Harmonious Subsequence.

코멘트: 
문제가 좋음. 
어려워 보여서 살짝 당황할 수 있음.
collections.Counter 를 떠올리면 절반 풀었음. 
colelctions.Counter 를 value 오름차순기준으로 정렬하는 법을 알면 다푼거임. 
'''
import collections
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c= sorted(collections.Counter(nums).items())
        total = 0 
        for t in range(1, len(c)):
            if c[t][0] - c[t - 1][0] == 1:
                if total < c[t][1] + c[t - 1][1]:
                    total = c[t][1] + c[t - 1][1]
        return total 
            


