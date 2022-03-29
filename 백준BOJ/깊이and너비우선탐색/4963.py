# 1020 
# https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<height and 0<=ny<width and graph[nx][ny] == 1:
            dfs(nx, ny) 

while True:
    width, height = map(int, input().split())
    if width == 0 and height == 0:
        break
    graph = []
    land = 0
    for _ in range(height):
        graph.append(list(map(int, input().split())))

    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1:
                dfs(i, j)
                land += 1
    print(land)
