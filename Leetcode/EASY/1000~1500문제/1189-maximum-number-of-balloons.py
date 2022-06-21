'''
1209 ~ 1247 
Runtime: 25 ms, faster than 99.24% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 14.1 MB, less than 13.24% of Python3 online submissions for Maximum Number of Balloons.

'''
from collections import defaultdict 
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        for c in text:
            d[c] += 1
        print(d)
        
        instances = 0 
        
        for c in text:
            if c not in d:
                return instances
        
        while True:
            count = 0
            for c in list('balloon'):
                d[c] -= 1
                if d[c] < 0:
                    return instances 
                count += 1
            if count != len('balloon'):
                return instances
            print(count)
            instances += 1
        
        return instances 
                    