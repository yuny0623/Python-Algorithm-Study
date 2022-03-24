'''
0946 <- 좋은 문제인듯 

슬라이딩 윈도우로 풀어야한다고 착각할 수도 있음.
근데 dp 써서 다이나믹 프로그래밍으로 푸는게 맞음. -> 정해 
'''

import sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n 
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    print(max(dp))