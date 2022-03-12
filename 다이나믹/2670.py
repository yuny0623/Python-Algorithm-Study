''' https://www.acmicpc.net/problem/2670
    연속 부분최대곱 ''' 
N = int(input())
li = [float(input()) for _ in range(N)]
for i in range(1, N):
    li[i] = max(li[i], li[i - 1] * li[i])
print("%.3f"%max(li))


