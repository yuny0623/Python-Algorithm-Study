'''
0400 ~ 0405 

Runtime: 139 ms, faster than 55.15% of Python3 online submissions for Find the Distance Value Between Two Arrays.
Memory Usage: 14 MB, less than 41.83% of Python3 online submissions for Find the Distance Value Between Two Arrays.

코멘트: 
딱히 어렵진 않음. not any 는 단 하나도 위배되면 안됨을 의미한다. 즉 전부다 만족해야함. 
'''

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # |arr1[i] - arr[j]| <= d //를 위배하는 어떤 element 도 없는 arr1의 element의 개수를 구하라. 
        counter = 0; 
        for i in range(len(arr1)):
            is_distance_val = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    is_distance_val = False
                    break 
            if is_distance_val:
                counter += 1
        
        return counter