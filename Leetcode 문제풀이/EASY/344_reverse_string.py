'''
0931 ~ 0939 
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = 1
        for i in range(len(s)//2):
            s[i], s[-k] = s[-k], s[i]
            k += 1
        print(s)