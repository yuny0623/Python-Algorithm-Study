'''
0949 
~
1035 
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline 

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, s):
    if len(s) == 6:
        if s not in result:
            result.append(s)
        return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, s + board[nx][ny]) 

board = []
for _ in range(5):
    board.append(list(map(str, input().split())))

result = [] 
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j]) 

print(len(result))