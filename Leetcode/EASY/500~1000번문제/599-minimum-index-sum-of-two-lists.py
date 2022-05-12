'''
0939 ~ 1000 
Runtime: 236 ms, faster than 49.90% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.3 MB, less than 88.91% of Python3 online submissions for Minimum Index Sum of Two Lists.

원리는 간단함.
근데 문제에 헷갈릴 여지가 있음. 
예시를 잘봐야 맞출 수 있음. 문제만 읽고 예시안보면 혼동할 여지가 큼.  
'''
from collections import defaultdict 
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # least list index sum -> 이게 중요함. 왜하는지 모르겠네. 인덱스가 거리순인가?
        same = list(set(list1) & set(list2)) 
        d = dict()
        for i in range(len(same)):
            d[same[i]] = list1.index(same[i]) + list2.index(same[i])
        
        min_val = min(d.values())
        
        result = []
        for key, value in d.items():
            if value == min_val:
                result.append(key)
        return result 
            
                    
