'''
0703 ~ 0709 
Runtime: 51 ms, faster than 91.16% of Python3 online submissions for Maximize Sum Of Array After K Negations.
Memory Usage: 14.1 MB, less than 16.71% of Python3 online submissions for Maximize Sum Of Array After K Negations.

코멘트: 
이 문제는 쉬운데 경우의 수를 나누어서 풀어야함.
음수가 있으면 양수로 만들어주고~ k가 홀수이면 가장 작은 원소 부호 하나만 바꿔주면 된다. 
k가 짝수이면? 어차피 양수 -> 음수 / 음수 -> 양수 로 다시 양수로 바꿔줄 수 있으니 연산안해도 된다. 
'''

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 이 문제는 쉬운데 경우의 수를 나누어서 풀어야함. 
        nums = sorted(nums)
        # nums에 음수가 있을 경우 
        for i in range(len(nums)):
            if k == 0:
                break 
            if nums[i] < 0: 
                nums[i] = -nums[i]
                k -= 1
        # k가 홀수일 경우 - 가장 작은 원소의 부호만 바꾼다. 
        if k%2 == 1: 
            nums = sorted(nums)
            nums[0] = -nums[0]
            return sum(nums)
        # k가 짝수일 경우 - 아무것도 하지 않아도됨. 
        else:
            return sum(nums)
