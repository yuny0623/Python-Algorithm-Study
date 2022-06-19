'''
0321 ~ 0341 

Runtime: 109 ms, faster than 5.17% of Python3 online submissions for Relative Sort Array.
Memory Usage: 14.4 MB, less than 5.85% of Python3 online submissions for Relative Sort Array.
'''

from collections import defaultdict 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_li = [] 
        d = defaultdict(int)
        for n in arr1:
            d[n] += 1
        
        print(d)
        for n in arr2: 
            print(n, d[n])
            print(new_li)
            new_li += [n] * d[n]
            d[n] = 0
        
        print(d)
        temp = [] 
        for k, v in d.items():
            if v != 0:
                print("here k,v:{0},{1}".format(k, v))
                temp += [k] * v
        return new_li + sorted(temp)
