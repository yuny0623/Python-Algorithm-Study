'''
0446 ~ 0451 

Runtime: 225 ms, faster than 77.30% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.9 MB, less than 5.79% of Python3 online submissions for Sort Array By Parity II.

코멘트: 
구현 문제 
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        even = []
        odd = []
        for n in nums:
            if n%2 == 0:
                even.append(n)
            else:
                odd.append(n)
        result = []
        e = 0
        o = 0
        for i in range(len(nums)):
            if i%2 == 0:
                result.append(even[e])
                e += 1
            else:
                result.append(odd[o])
                o += 1
                
        return result 
            
