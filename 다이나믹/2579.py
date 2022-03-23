'''
0354 
~
0434 
https://www.acmicpc.net/problem/2579

112
12
222 

'''


import sys
input = sys.stdin.readline 
n = int(input())

d = [0 for _ in range(301)]
step = [0 for _ in range(301)]

for i in range(n):
    step[i] = int(input())

d[0] = step[0]
d[1] = step[0] + step[1]
d[2] = max(step[1] + step[2], step[0] + step[2])
for i in range(3, n):
    d[i] = max(d[i - 3] + step[i-1] + step[i], d[i-2] + step[i])
print(d[n - 1])