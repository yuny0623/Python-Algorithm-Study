# 0823 ~ 0858 
# 백준 1012 
import sys
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    # M: 가로길이, N: 세로길이, K: 배추개수 
    # X            Y 
    g = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        g[j][i] = 1 
    
    worm = 0 
    for i in range(M): # 세로 길이 -> X
        for j in range(N): # 가로 길이  -> Y
            stack = []
            stack.append((i,j))
            if i <= -1 or i>= N or j<= -1 or j >= M:
                worm += 0 
            while stack:
                i, j = stack.pop()
                if g[i][j] == 1:
                    g[i][j] = 0
                    stack.append((i - 1, j)) # 상 
                    stack.append((i + 1, j)) # 하
                    stack.append((i, j - 1)) # 좌
                    stack.append((i, j + 1)) # 우
                    worm += 1
    print(worm)


