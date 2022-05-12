'''
0826 ~ 0934 

예외조건이 좀 까다로움. 어려운데 뭐지. -> 맨 아래 정답 솔루션 있음. 
'''
'''
이건 아예 오답. -> 여기서 Time Limit, Memory Limit 이 발생함. 아예 접근법이 틀렸다는 얘기.
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        # 두 문제가 겹쳐있는 문제인듯 
        M = [[0] * n for _ in range(m)]
        
        # 첫번째 부분 문제 
        for o in ops:
            a = o[0] 
            b = o[1]
            for i in range(a):
                for j in range(b):
                    M[i][j] += 1
        
        # 두번째 부분 문제 
        flat_M = []
        for i in range(m):
            for j in range(n):
                flat_M.append(M[i][j])
        max_value = max(flat_M)
        print(max_value)
        
        return flat_M.count(max_value)



'''
두번째 솔루션 : 
이것도 틀렸음
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        freq_area = min(ops)
        return freq_area[0] * freq_area[1]

'''
정답 솔루션 

Runtime: 134 ms, faster than 16.76% of Python3 online submissions for Range Addition II.
Memory Usage: 16 MB, less than 80.75% of Python3 online submissions for Range Addition II.

코멘트: 
원리를 알아야 쉽게 풀 수 있음. x값 최소, y값 최소를 구한게 최소 영역 -> 가장 빈번한 영역이다. 
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        flat_x = []
        flat_y = []
        for o in ops:
            flat_x.append(o[0])
            flat_y.append(o[1])
        min_x = min(flat_x)
        min_y = min(flat_y)
        return min_x * min_y
        
