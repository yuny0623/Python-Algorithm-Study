'''
0457 ~ 0502 
'''
import sys
input = sys.stdin.readline 
n = int(input())

d = [0] * 116

d[0] = 1
d[1] = 1
d[2] = 1
for i in range(3, n):
    d[i] = d[i - 1] + d[i - 3]

print(d[n-1])

