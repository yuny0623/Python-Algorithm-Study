# 0338 
import sys
sys.setrecursionlimit(10**7)
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)] 


def dfs(x, y):

    if x<= -1 or x>= N or y<= -1 or y>= N:
        return False

    value = graph[x][y]
    if value == -1:
        print("HaruHaru")
        exit(0)

    if visited[x][y] != True:
        visited[x][y] = True
        dfs(x + value, y) # 하 
        dfs(x, y + value) # 우     

dfs(0,0)
print("Hing")

'''
해결은 했지만, 별로 좋지 못한 코드다
exit(0)으로 바로 빠져나왔지만, 감점의 요지가 있다. 
다른 방식이 필요함. 

'''