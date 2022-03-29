'''
1155 

0145 

각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
# 시간초과가 뜨네요 . 
'''

from itertools import count
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):

    N = int(input())
    d_0 = [0] * (40 + 1)
    d_1 = [0] * (40 + 1)
    d = [0] * (40 + 1)

    d_0[0] = 1
    d_1[1] = 1

    for x in range(2, N + 1):
        d_0[x] = d_0[x - 1] + d_0[x - 2]
    for x in range(2, N + 1):
        d_1[x] = d_1[x - 1] + d_1[x - 2]
    
    print(d_0[N], d_1[N]) 
