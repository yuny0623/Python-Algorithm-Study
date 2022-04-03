'''
0931 ~ 0939 
이건 s[::-1] 로는 안풀린다. 
직접 바꿔줘야함. 
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