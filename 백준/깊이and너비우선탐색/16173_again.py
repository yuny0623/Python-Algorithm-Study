'''
0451 ~ 

'''

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if not (0<=x<n and 0<=y<n):
        return

    if visited[x][y]: # 방문한 곳이면 return
        return

    if board[x][y] == -1:
        print("HaruHaru")
        exit(0)

    step = board[x][y]
    if not visited[x][y]: # 방문하지 않은 곳이라면
        visited[x][y] = True
        dfs(x + step, y)
        dfs(x, y + step)

dfs(0, 0)
print('Hing')