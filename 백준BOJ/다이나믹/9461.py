'''
1039 
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = [1] * 100
    d[1] = 1
    d[2] = 1
    d[3] = 2
    d[4] = 2
    d[5] = 3
    for i in range(6, n):
        d[i] = d[i - 1] + d[i - 5]
    print(d[n - 1])