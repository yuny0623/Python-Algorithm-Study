'''
0737 ~ 0745 
Runtime: 75 ms, faster than 34.17% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 48.44% of Python3 online submissions for Reverse Words in a String III.

이거 follow up이 아무것도 없는데, extra space 없이 결과내라고 하면 풀 수 있나. 
추가 메모리 없으면 난이도 많이 올라갈듯 
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        li = list(s.split(' '))
        if len(li) == 1:
            return s[::-1]
        result = []
        for w in li:
            result.append(w[::-1])
        
        return ' '.join(result)

