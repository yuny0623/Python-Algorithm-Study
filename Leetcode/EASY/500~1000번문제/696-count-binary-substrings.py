'''
0913 ~ 
0230 ~ 0350 
Runtime: 126 ms, faster than 98.10% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 15.9 MB, less than 5.53% of Python3 online submissions for Count Binary Substrings.

코멘트:
생각보다 어려워. 경험해본적이 없으면 풀기 힘들듯. 
그리고 풀 수 있는 방법이 여러 개임. 
'''

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Using the map function to find the combined length of 0 and 1 that are cut apart
        L = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split('')))
        #Because it is limited that only 0 and 1 can be next to each other, only adjacent ones can team up, using the zip function
        res = sum(min(a,b) for a,b in zip(L, L[1:]))
        return res



