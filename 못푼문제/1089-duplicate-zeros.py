'''
0123 ~ <답지보고 풀음>

코멘트: 
답지보고 풀었다. 그런데 방법이 너무 기발하다. 
https://www.youtube.com/watch?v=gaB-guUxCWI

Runtime: 113 ms, faster than 45.54% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 15 MB, less than 25.03% of Python3 online submissions for Duplicate Zeros.

'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = [] 
        for i in range(len(arr)):
            if arr[i] == 0:
                queue.append(0)
                queue.append(0)
            else:
                queue.append(arr[i])
            arr[i] = queue.pop(0)
            
                    





