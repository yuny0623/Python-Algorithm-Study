from collections import deque 
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
graph = []

for _ in range(R):
    graph.append(list(input().rstrip()))

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global w, s

    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == 'k':
            s += 1
        if graph[x][y] == 'v':
            w += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<R and 0<=ny<C and graph[nx][ny] != '#' and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

wolf = 0
sheep = 0 

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j] == 0:
            w = 0 # 늑대 
            s = 0 # 양 

            bfs(i, j)

            if w >= s:
                s = 0
            else:
                w = 0

            wolf += w
            sheep += s 

print(sheep, wolf)