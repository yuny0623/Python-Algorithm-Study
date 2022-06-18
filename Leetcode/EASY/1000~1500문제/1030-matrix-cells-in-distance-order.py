'''
0802 ~ 0810 
Runtime: 310 ms, faster than 20.19% of Python3 online submissions for Matrix Cells in Distance Order.
Memory Usage: 17 MB, less than 13.54% of Python3 online submissions for Matrix Cells in Distance Order.

코멘트: 
왜 lambda 에서는 인수에 요소 변경이 적용이 안될까... 
'''

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        dist_li = []
        for i in range(rows):
            for j in range(cols):
                dist = abs(rCenter - i) + abs(cCenter - j)
                dist_li.append([i, j, dist])
        
        dist_li = sorted(dist_li, key = lambda x: x[2])
        return [x[:2] for x in dist_li ]
        
        



