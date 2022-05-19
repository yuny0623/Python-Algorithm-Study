'''
0816 ~ 0827  <답지보고 풀음>

Runtime: 95 ms, faster than 75.21% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.8 MB, less than 79.93% of Python3 online submissions for Toeplitz Matrix.

코멘트:
너무 어렵게 생각해서 접근을 못했다. 답지를 보니 좀 허무하네. 
익숙한데 어렵게 느껴지면 오랜만에 봐서 그런거다. 그냥 직관적으로 풀자.
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                
        return True 
            
                                   
            




