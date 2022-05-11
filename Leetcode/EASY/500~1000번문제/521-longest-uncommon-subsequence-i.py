'''
0933 ~ 0958 

Runtime: 46 ms, faster than 36.65% of Python3 online submissions for Longest Uncommon Subsequence I.
Memory Usage: 13.9 MB, less than 64.52% of Python3 online submissions for Longest Uncommon Subsequence I.

문제가 제대로 해석한게 맞는지 의문. 문제는 굉장히 긴 지문인데
따지고 보면 경우의 수가 몇 안되서 그냥 조건문만 몇개 써줘도 풀 수 있음.
그리 좋은 문제는 아닌듯. 
'''
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return len(a)
        if len(a) < len(b):
            return len(b) 
        if set(a) == set(b) and len(set(a)) < len(a):
            return -1 
        if set(a) == set(b):
            return len(a) 
        return len(a)