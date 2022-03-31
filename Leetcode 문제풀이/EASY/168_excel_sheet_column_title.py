'''
1048  ~ 1116 

26진수로 나타내기? 

답지보고 풀음 
''' 
class Solution:
    def convertToTitle(self, n):
        str = ''
        while n != 0: 
            tmp = chr(ord('A') + (n-1) % 26)
            n = (n-1) // 26
            str = tmp + str
        return str