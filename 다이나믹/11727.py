'''
1035 
~ 
1112 
체감 난이도가 많이 어려운듯 
점화식 생각 못하면 못품. 
'''

n = int(input())
dp = [0] * 1001 
dp[1] = 1
dp[2] = 3
for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007 
print(dp[n])


