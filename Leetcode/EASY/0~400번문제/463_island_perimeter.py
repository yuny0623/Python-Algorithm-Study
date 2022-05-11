'''
0316 ~ 

재밌는 문제인듯. 
재밌는 응용임. 

모르겠네 뭐냐 이거 ㅠㅠ 
~ 0424 
헤맸네. bfs 안쓰고 그냥 이렇게 풀 수도 있음. 이게 더 낫네. 
2씩 빼는이유? 두 영역이 맞닿아있으면 둘레에서 -2 를 해야함.
왜냐면 각 영역이 서로 변을 맞대고 있으니 서로 -1 씩 손해보니 -2를 해줘야함.  
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0 
        m, n = len(grid), len(grid[0])
        if m == 0 and n == 0:
            return 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0  and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0  and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter
    
    
    
    


