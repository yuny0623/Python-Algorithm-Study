'''
1041 
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline 

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)] 
graph[0] = [0, 0]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort() 

def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]: 
            dfs(graph, i, visited)

count = 0 
for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited)

print(count)
