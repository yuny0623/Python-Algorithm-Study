# 211 
# https://assaeunji.github.io/python/2020-05-06-bj1236/

n, m  = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

row = []
col = []

for i in range(n):
    row.append('X' not in arr[i])

for j in range(m):
    col.append('X' not in [arr[i][j] for i in range(n)])

print(max(sum(row), sum(col)))



