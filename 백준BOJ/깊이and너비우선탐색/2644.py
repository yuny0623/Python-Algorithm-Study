# 318

# bfs 방식 
from collections import deque 
from sys import stdin, stdout 

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                queue.append(n)

n = int(input())
a, b = map(int, input().split())
m = int(input())
check = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

bfs(a) # a 부터 시작해서 
print(check[b] if check[b] > 0 else -1) # b 까지 가보자 .


# 이 문제는 dfs 방식으로도 풀 수 있음.

import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)


