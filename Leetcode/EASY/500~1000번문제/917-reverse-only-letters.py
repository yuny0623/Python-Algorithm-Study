'''
0302 ~ 0310 
Runtime: 24 ms, faster than 97.97% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 13.9 MB, less than 64.76% of Python3 online submissions for Reverse Only Letters.

코멘트: 구현문제.
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        pos = []
        alpha = []
        for i in range(len(s)):
            if not s[i].isalpha():
                pos.append(i)
            else:
                alpha.append(s[i])
        
        alpha = alpha[::-1]
        result = [0 for _ in range(len(s))]
        
        for p in pos:
            result[p] = s[p]
        print(result)
        
        j = 0
        for i in range(len(s)):
            if result[i] != 0:
                continue
            else:
                result[i] = alpha[j]
                j += 1
                
        print(result)
        return ''.join(result)
        