'''
0908 

체스판 다시 칠하기 
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(input().rstrip()))

count = [] 
for i in range(N - 7):
    for j in range(M - 7):
        count_w = 0
        count_b = 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0: # 짝수 
                    if board[k][l] != 'W':
                        count_w += 1
                    if board[k][l] != 'B':
                        count_b += 1
                else:                # 홀수 
                    if board[k][l] != 'B':
                        count_w += 1
                    if board[k][l] != 'W':
                        count_b += 1

        count.append(min(count_b, count_w))

print(min(count))



