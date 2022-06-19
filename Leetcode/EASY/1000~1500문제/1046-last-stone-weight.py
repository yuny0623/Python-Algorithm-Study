'''
0911 ~ 0916 

Runtime: 47 ms, faster than 47.56% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.8 MB, less than 62.02% of Python3 online submissions for Last Stone Weight.
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 가장 무거운 2개의 stone 을 고른다. 
        while len(stones) > 1: 
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            if x != y:
                if x > y:
                    stones.append(x - y)
                else:
                    stones.append(y - x)
                    
        if len(stones) == 0:
            return 0 
        return stones[0]


'''
sol2
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 가장 무거운 2개의 stone 을 고른다. 
        while len(stones) > 1: 
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(x - y) if x > y else stones.append(y - x)
                
        if len(stones) == 0:
            return 0 
        return stones[0]