'''
0504 ~ 답지보고 풀음. 0538 


'''

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n):
    for j in range(i + li[i][0], n + 1):
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]

print(dp[-1])

