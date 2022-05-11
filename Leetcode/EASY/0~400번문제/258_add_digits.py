'''
1147  ~ 1151 
'''
class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) != 1:
            total = sum(list(map(int, list(s))))
            s = list(str(total))
        return s[0] 
            