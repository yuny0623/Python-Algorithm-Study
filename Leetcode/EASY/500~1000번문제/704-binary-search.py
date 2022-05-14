'''
0321 ~ 0325 
Runtime: 259 ms, faster than 76.68% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 23.25% of Python3 online submissions for Binary Search.

코멘트:
이 문제는 코멘트할게 없다...  라고 했지만 할게 너무 많다. 
무심코 아래 코드처럼 구현했다. 
근데 문제의 이름이 Binary Search 이다. 그러니 문제에서 원하는대로 풀어줘보자. 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1 
        else:
            return nums.index(target)

'''
정석 풀이: 
Runtime: 258 ms, faster than 77.58% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 23.25% of Python3 online submissions for Binary Search.

코멘트:
1ms줄었다. 그런데 이거 시간이 돌릴때마다 다른데 만약 실제로 이런 문제를 푼다면
위처럼 푸는게 좋을까 아니면 아래처럼푸는게 좋을까? 분명 위가 더 성능이 좋을텐데 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start =0 
        end = len(nums) - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid + 1
            if target < nums[mid]:
                end = mid - 1
        
        return -1


