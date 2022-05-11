'''
0333 
~
0517 

1. A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 
    하지만 상대 역시 3점을 득점하는 위험이 있다.
2. B는 1점을 얻는 연속 발차기이다.
'''
from collections import deque
import sys
input = sys.stdin.readline 

def bfs(s, t):
    q = deque()
    q.append((s, t, 0))
    check = [-1] * (200)
    while q: 
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c + 1))
            q.append((node + 1, t, c + 1))
            if node == t:
                return c 


T = int(input())
for _ in range(T):
    s, t = map(int, input().split()) # 현재 점수 s, 상대 점수 t 
    print(bfs(s, t))
