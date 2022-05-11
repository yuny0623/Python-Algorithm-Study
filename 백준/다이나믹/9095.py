'''
1003 
~
1038 
'''

import sys
input = sys.stdin.readline 
T = int(input())
for _ in range(T):
    t = int(input())
    d = [0] * 11 
    d[0] = 1
    d[1] = 2
    d[2] = 4 
    for i in range(3, t + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[t - 1])

