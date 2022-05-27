'''
1128 ~ <밥먹고옴ㅋ> ~ <답지보고품.>
Runtime: 98 ms, faster than 78.97% of Python3 online submissions for Surface Area of 3D Shapes.
Memory Usage: 13.9 MB, less than 95.79% of Python3 online submissions for Surface Area of 3D Shapes.

코멘트: 수학문제네.
규브 더해졌을때의 규칙같은걸 알아야 풀 수 있을듯 

천장 바닥 -> 미리 +2 를 계산해준다. 
그리고 상하좌우를 각각 조건으로 검사해주면서 surface 갯수 알아내면 된다. 
좋은문제네 
'''
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0 
        total_surface = 0 
        n = len(grid)
        for i in range(n):
            for j in range(n):
                height = grid[i][j]
                surface = 2 + 4 * height if height > 0 else 0
                
                if i != n - 1:
                    surface -= min(height, grid[i + 1][j])
                if i != 0:
                    surface -= min(height, grid[i - 1][j])
                if j != n - 1:
                    surface -= min(height, grid[i][j + 1])
                if j != 0:
                    surface -= min(height, grid[i][j - 1])
                total_surface += surface
                
        return total_surface
