'''
0324 ~ 0359 

이상한 에러가 발생해서 많이 늦어짐. 

아래는 오답임. 뭐가 문제일까...  
팁:
밑에 새로 해결한 솔루션 있음. 
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # mat: m * n -> r * c
        # 못바꾸면 기존 matrix 를 리턴하세요 
        print("r:{0}".format(r))
        print("c:{0}".format(c))
        if len(mat) * len(mat[0]) != r * c: # 바꿀 수 없으면 기존 매트릭스 리턴 
            return mat 
        result = [[0] * c] * r 
        print("result:{0}".format(result))
        for i in range(r):
            for j in range(c):
                print("print:{0}".format(result[i][j]))
        # r = 4
        # c = 1
        # 1 2 
        # 3 4 
        flat_data = [] 
        for i in range(len(mat)): # 1 
            for j in range(len(mat[0])): # 2 
                flat_data.append(mat[i][j])
        print("flat_date:{0}".format(flat_data)) # 1 2 3 4 
        
        idx = 0 
        for k in range(r): # 4 
            for l in range(c):  # ! 
                print("result:{0}, r:{1}, c:{2}".format(result, k, l))
                result[k][l] = flat_data[idx] # (0, 0)(1, 0), (2, 0) (3, 0)
                idx += 1
                
        print(idx)
        return result 

'''
정답판정 
이렇게 하니까 풀렸다. 
위랑 같은 로직인데 대체 뭐가 다른걸까요 

Runtime: 102 ms, faster than 70.17% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 14.8 MB, less than 37.00% of Python3 online submissions for Reshape the Matrix.

result 를 선언하는 방식을 list comprehension 으로 바꾼건데 그게 그냥 선언 방식이 다른건데 정답에 
영향을 미치나? 
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # mat: m * n -> r * c
        # 못바꾸면 기존 matrix 를 리턴하세요 
        if len(mat) * len(mat[0]) != r * c:
            return mat 
        
        flat_mat = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                flat_mat.append(mat[i][j])
        print("flat_mat:{0}".format(flat_mat))

        result = [[0]*c for _ in range(r)] 
        
        idx = 0
        for i in range(r):
            for j in range(c):
                result[i][j] = flat_mat[idx] 
                idx += 1 
        print("result:{0}".format(result))

        return result 