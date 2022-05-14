'''
1030 ~ 1046 

Runtime: 1125 ms, faster than 12.75% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.4 MB, less than 55.21% of Python3 online submissions for Degree of an Array.

코멘트: 
좀 지저분하게 풀었던 문제. 로직은 맞는데 가독성만 좀 손보면 될듯 
'''
from collections import defaultdict 
import sys 
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        print(d)
        max_freq = 0
        freq_key = 0
        for key, value in d.items():
            if value > max_freq:
                max_freq = value 
                freq_key = key 
        print(max_freq)
        print(freq_key)

        freq_list = []
        for key, value in d.items():
            if value == max_freq:
                freq_list.append(key)
        print(freq_list)
        smallest_sub_length= sys.maxsize
        li = []
        for f in freq_list:
            start = nums.index(f)
            end = len(nums) - nums[::-1].index(f)
            li.append(end - start)
        print("li:{0}".format(li))
        return min(li)
            
            
'''
가독성 개선한 솔루션:  
Runtime: 947 ms, faster than 15.36% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.4 MB, less than 83.59% of Python3 online submissions for Degree of an Array.

아래 코드에서 로직을 개선할 수 있을까? 
'''

from collections import defaultdict 
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        max_freq = 0
        freq_key = 0
        for key, value in d.items():
            if value > max_freq:
                max_freq = value 
                freq_key = key 

        freq_list = []
        for key, value in d.items():
            if value == max_freq:
                freq_list.append(key)
        li = []
        for f in freq_list:
            start = nums.index(f)
            end = len(nums) - nums[::-1].index(f)
            li.append(end - start)
        return min(li)
            
'''
로직 개선한 코드: 
'''



            