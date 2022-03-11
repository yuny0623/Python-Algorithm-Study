# 0909 
# 조합을 알면 쉽게 풀 수 있는 문제다. 
n, k = map(int, input().split())

memo = [[0]*30 for i in range(30)]
memo[1][1] = 1
def binomial(n, r):

    if (n == r or r == 0):
        memo[n][r] = 1
        return memo[n][r]

    if memo[n][r] != 0:
        return memo[n][r]

    memo[n][r] = binomial(n - 1, r - 1) + binomial(n - 1, r)
    return memo[n][r]

print(binomial(n - 1, k - 1))
print(memo)
    