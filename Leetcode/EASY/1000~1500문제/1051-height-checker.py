'''
1116 ~ 1228 
Runtime: 73 ms, faster than 11.67% of Python3 online submissions for Height Checker.
Memory Usage: 13.8 MB, less than 53.33% of Python3 online submissions for Height Checker.
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0 
        for a, b in zip(heights, expected):
            if a!= b:
                counter += 1
        return counter 




