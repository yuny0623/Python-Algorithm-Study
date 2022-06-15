'''
0921 ~ 0940 

Runtime: 187 ms, faster than 34.23% of Python3 online submissions for Smallest Range I.
Memory Usage: 15.2 MB, less than 89.21% of Python3 online submissions for Smallest Range I.

코멘트: 
'''
'''
오답 솔루션1: 
첫번째 접근방법: 로직이 틀림. 자 그렇다면 어떻게 접근해야 풀릴까? 
'''
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)  # 0, 10 
        
        for i in range(k): # 2 -> 0, 1 
            nums[i] += k - i
            if i >= (len(nums) - 1) // 2:
                break 
        print(nums)
        for i in range(k):
            nums[len(nums) - 1 - i] -= k - i
            if i >= (len(nums) - 1) // 2:
                break 
        print(nums)
        
        return max(nums) - min(nums)

'''
정답 판정 솔루션: 
간단하다. 중앙값을 찾아놓고 요소가 그 값보다 크다면? 줄여주자. 만약 중앙값보다 작다면? 더해서 크게 만들어주자.
모든 요소를 순회하면서 최대한 모든 요소가 중앙값과 가까워지게 만들어야 max와 min의 차이가 줄어들겠지? 아래와 같이 풀자. 
'''
            

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)  # 0, 10 
        mid = (max(nums) + min(nums)) // 2 
        
        for i in range(len(nums)):
            if nums[i] < mid: # 중간값보다 작다면 
                if mid - nums[i] > k:
                    nums[i]+= k
                else:
                    nums[i] = mid 
            if nums[i] > mid: # 중간값보다 크다면 
                if nums[i] - mid > k:
                    nums[i] -= k
                else:
                    nums[i] = mid
        
        print(nums)
        return max(nums) - min(nums)