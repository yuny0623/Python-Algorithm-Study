'''
0215 ~ 0230 

Runtime: 96 ms, faster than 56.46% of Python3 online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 15.7 MB, less than 11.67% of Python3 online submissions for Longest Continuous Increasing Subsequence.

코멘트: 
마지막 요소까지 오름차순 되어있다면 for 문 밖에서 다시한번 max_length 랑 비교를 해줘야함. 
'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # strictly increasing 이다. 값이 같은건 소용없어요. 무조건 커야되 
        max_length = 1
        length  = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 1
                
        if length > max_length:
            max_length = length
        if len(list(set(nums))) == 1:
            return 1
        return max_length 

'''
solution2: 
Runtime: 112 ms, faster than 38.44% of Python3 online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 15.4 MB, less than 11.67% of Python3 online submissions for Longest Continuous Increasing Subsequence.
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 1
        length  = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 1
        if length > max_length:
            max_length = length
        return max_length 
