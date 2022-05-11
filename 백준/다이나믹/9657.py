'''
1119 
마지막 돌을 가져가는 사람이 게임을 이기게 된다.

'''

n = int(input())
dp = [0] * 1001 
dp[1] = 1
dp[3] = 1
dp[4] = 1
if n >= 5:
    for i in range(5, n + 1):
        if not dp[i - 1]:
            dp[i] = 1
        if not dp[i - 3]:
            dp[i] = 1
        if not dp[i - 4]:
            dp[i] = 1

if dp[n]:
    print("SK")
else:
    print("CY")
