'''
0123 ~ <답지보고 풀음>

코멘트: 
큐 사용해서 구현해보자 

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
            
                    





