'''
0106 ~ 0135 

Runtime: 107 ms, faster than 43.46% of Python3 online submissions for Flood Fill.
Memory Usage: 14.5 MB, less than 14.90% of Python3 online submissions for Flood Fill.

코멘트: 
처음엔 bfs 로 풀려고 했는데 오히려 dfs 로 푸는게 좀더 쉽겠다고 판단함. 
근데 아마 bfs 로도 가능할것 같긴하다. 구현 그대로다. 범위만 좀 잘 잡아주고 풀면 된다. 

이거 근데 visited 없어도 풀릴 것 같은데? 
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        height = len(image)
        weight = len(image[0])
        visited = [[0 for _ in range(weight)] for _ in range(height)]
        print(visited)
        
        def dfs(x, y):
            if not (0 <= x <= height -1 and 0 <= y <= weight -1):
                return 
            if visited[x][y] == 1:
                return     
            if image[x][y] != starting_color:
                return 
            
            image[x][y] = newColor 
            visited[x][y] = 1
            
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        dfs(sr,sc)
        
        return image 

'''
visited 없앤 솔루션:

'''