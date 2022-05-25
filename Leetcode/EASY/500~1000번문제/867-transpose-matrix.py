'''
0454 ~ 0456 
Runtime: 83 ms, faster than 68.27% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.7 MB, less than 55.74% of Python3 online submissions for Transpose Matrix.

코멘트: 
신박한 문제임. 이중 for 문 안과 밖 거꾸로 바꿔서 써주면 쉽게 풀림. 
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [] 
        for j in range(len(matrix[0])):
            new_row = [] 
            for i in range(len(matrix)):
                new_row.append(matrix[i][j])
            transpose.append(new_row)
        return transpose 
                