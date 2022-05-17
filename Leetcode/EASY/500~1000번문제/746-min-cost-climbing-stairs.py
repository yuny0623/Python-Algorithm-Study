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