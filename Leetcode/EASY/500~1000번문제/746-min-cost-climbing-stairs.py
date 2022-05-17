'''
0920 ~ <답지보고 풀음>

코멘트: 
dp 문제임. 좋은문제임. 

Runtime: 79 ms, faster than 50.39% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 13.8 MB, less than 97.56% of Python3 online submissions for Min Cost Climbing Stairs.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])

'''
Runtime: 93 ms, faster than 32.27% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 13.9 MB, less than 97.56% of Python3 online submissions for Min Cost Climbing Stairs.

또다른 솔루션:
아래 방식으로도 가능함. 대신 이건 밑에서부터 위로 올라가는 코드임. 위 코드는 뒤쪽 인덱스부터 내려오는 형식임. 
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])
        return min(dp[-1], dp[-2])