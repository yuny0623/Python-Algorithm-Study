'''
0955 ~ 0959 

Runtime: 1488 ms, faster than 7.05% of Python3 online submissions for Distribute Candies.
Memory Usage: 16.3 MB, less than 38.54% of Python3 online submissions for Distribute Candies.

쉬운 문제. 
속도가 좀 느리게 나왔는데 개선 가능? 
'''

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = len(list(set(candyType)))
        n = len(candyType)//2
        return min(s, n)
        
'''
개선한 코드
Runtime: 842 ms, faster than 82.65% of Python3 online submissions for Distribute Candies.
Memory Usage: 16.4 MB, less than 9.15% of Python3 online submissions for Distribute Candies.
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = len(set(candyType))
        n = len(candyType)//2
        return min(s, n)
'''
'''
    

        