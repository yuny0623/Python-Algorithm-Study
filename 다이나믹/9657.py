'''
1119 
마지막 돌을 가져가는 사람이 게임을 이기게 된다.
'''

n = int(input())
dp = [False] * (n + 1)
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True
dp[5] = True
for i in range(6, n + 1):
    dp[i] = not(dp[i - 1] and dp[i - 3] and dp[i -4])

if dp[n - 1] == True:
    print("SK")
else:
    print("CY")
