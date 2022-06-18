'''
0746 ~ 0755 

Runtime: 1428 ms, faster than 21.46% of Python3 online submissions for Binary Prefix Divisible By 5.
Memory Usage: 16.5 MB, less than 10.47% of Python3 online submissions for Binary Prefix Divisible By 5.

코멘트: 
'''

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums = ''.join(list(map(str, nums)))
        if len(nums) == 1:
            return True if int(nums[0], 2)%5 == 0 else False 
        
        l = len(nums)
        i = 1
        answer = [] 
        while i <= l: 
            answer.append(True) if int(str(nums[:i]), 2)%5 == 0 else answer.append(False)
            i += 1
            
        return answer

'''
더 짧은 풀이 
Runtime: 1407 ms, faster than 21.99% of Python3 online submissions for Binary Prefix Divisible By 5.
Memory Usage: 15.2 MB, less than 43.46% of Python3 online submissions for Binary Prefix Divisible By 5.
'''
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary_str = ''
        answer = []
        for num in nums:
            binary_str += str(num)
            answer.append(True) if int(binary_str, 2)%5 == 0 else answer.append(False)
        return answer 