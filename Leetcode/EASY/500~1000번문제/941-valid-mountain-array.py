'''
0533 ~ 0540 

Runtime: 214 ms, faster than 88.76% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.8 MB, less than 20.74% of Python3 online submissions for Valid Mountain Array.

코멘트: 
문제 자체는 쉬움. 다만 예외 케이스들이 있는데 그것만 잡우주면 됨. 
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # 길이가 3 미만이면 False 
            return False
        
        # 오직 오르막길만 있으면 False
        if arr == sorted(arr):
            return False 
        # 오직 내리막길만 있으면 False 
        if arr == sorted(arr, reverse = True):
            return False 
        
        peak = arr.index(max(arr))
        
        high = arr[:peak]
        low = arr[peak:]
        
        if high == sorted(list(set(arr[:peak]))) and low == sorted(list(set(arr[peak:])), reverse=True):
            return True
        return False 
        
        

