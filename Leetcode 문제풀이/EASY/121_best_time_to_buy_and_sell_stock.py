'''
0623 - 0638 ~ 0650 
브루트 포스로 풀었다가 Time limit exceeded 이 발생했다. 
아래 방식처럼 풀어라. 그래야 시간초과 안뜸. 
'''

import sys
from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신 
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit




