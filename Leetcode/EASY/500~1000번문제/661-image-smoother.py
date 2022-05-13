'''
0128 ~ 0150 

Runtime: 856 ms, faster than 42.69% of Python3 online submissions for Image Smoother.
Memory Usage: 14.8 MB, less than 37.03% of Python3 online submissions for Image Smoother.

코멘트: 
keypad 혹은 좌표 문제가 나오면 아래 eight_side에 정의된것과 같은 좌표계를 적극 활용하면 보통 쉽게 풀림. 

개선할 부분들이 몇군데 보임. 개선해보자. 
'''

import math 
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # 지문이 조금... 
        r = len(img)
        c = len(img[0])
        result = [[0] * c for _ in range(r)]
        
        eight_side = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        def square_sum(i, j):
            total = 0
            count = 1 
            for s in eight_side:
                if i + s[0] < r and i + s[0] >= 0 and j + s[1] < c and j + s[1] >= 0:
                    total += img[i + s[0]][j + s[1]]
                    count += 1
            total += img[i][j]
            return math.floor(total / count)
              
        for i in range(r):
            for j in range(c):
                result[i][j] = square_sum(i, j)
                        
        return result 
    
'''
개선한 코드: 
Runtime: 721 ms, faster than 64.86% of Python3 online submissions for Image Smoother.
Memory Usage: 14.7 MB, less than 37.03% of Python3 online submissions for Image Smoother.
'''
import math 
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])
        result = [[0] * c for _ in range(r)]
        
        eight_side = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        def square_sum(i, j):
            total = 0
            count = 1 
            for s in eight_side:
                if 0 <= i + s[0] < r and 0 <= j + s[1] < c :
                    total += img[i + s[0]][j + s[1]]
                    count += 1
            total += img[i][j]
            return total // count
            
        for i in range(r):
            for j in range(c):
                result[i][j] = square_sum(i, j)
                        
        return result 
    




