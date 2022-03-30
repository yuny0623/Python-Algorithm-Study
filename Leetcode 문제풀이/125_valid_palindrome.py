'''
0804 ~ 0820 
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.split()
        new_str = ''.join(new_str).lower()
        result = []
        for c in new_str:
            if c.isalpha() or c.isdigit():
                result.append(c)
                    
        new_str = ''.join(result)
        if len(new_str) == 1 or len(new_str) == 0:
            return True
        
        valid = True
        for i in range(len(new_str) // 2):
            if new_str[i] == new_str[len(new_str) - 1 - i]:
                continue
            else:
                valid = False
                
        return valid 