'''
0255  ~ 0342 <답지보고풀음>

Runtime: 301 ms, faster than 16.90% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.5 MB, less than 91.39% of Python3 online submissions for Valid Palindrome II.

코멘트: substring 으로 분할해서 푸는게 가장 효율적임 
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        
        def is_valid(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True 
        
        while front < back:
            if s[front] != s[back]:
                return is_valid(s, front + 1, back) or is_valid(s, front, back - 1)
            front += 1
            back -= 1
        return True 
        
        


    




