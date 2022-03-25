'''
0518 
~
메모리 초과 뭐죠? ㄷㄷ 
~ 0629 
'''

# import sys
# from collections import deque
# input = sys.stdin.readline 

# def bfs(i):
#     cnt = 0 
#     q = deque()
#     q.append(i)
    
#     while q: 
#         pos = q.popleft() 

#         for i in range(1, arr[pos] + 1):
#             jump = pos + i 
#             if jump < n : 
#                 q.append(jump)
#                 cnt += 1
#         if pos == len(arr) - 1:
#             return cnt 
#     return -1 

# n = int(input())
# arr = list(map(int, input().split()))

# print(bfs(0))


'''
0518 
~ 0611 

파이썬에서는 뭐가됬든 메모리 마구 쓰지 맙시다. 
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 1이라면 시작과 동시에 종료
if n == 1:
    print(0)
    sys.exit()
    
arr = list(map(int,input().split()))
visited = [0]*n
q = deque([(0,arr[0])]) # 현재 위치, 점프 가능 거리

while q:
    pos,jump = q.popleft()
    for i in range(1,jump+1):
        if pos+i >= n or visited[pos+i]:
            continue
        visited[pos+i] = visited[pos]+1
        q.append((pos+i,arr[pos+i]))

print(visited[-1] if visited[-1] else -1)