'''
0437 ~ 0443
Runtime: 8258 ms, faster than 5.74% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.1 MB, less than 93.59% of Python3 online submissions for Find Pivot Index.

코멘트: 
처음엔 sum 구한 다음에 반복 돌면서 index 요소 빼주면서 2로 나뉘지는지 체크했었는데
문제 잘 읽어보니까 그냥 왼쪽 오른쪽 sum 만 똑같으면 됨. 
그런데 지금 코드가 8000ms가 나옴. 이거 좀더 개선할 수 있지 않을까? 
지금 드는 생각에 sliding window 방식으로 개선할 수 있을것 같은데? 
대신 윈도우가 가운에 하나가 아니라 왼쪽 오른쪽 2개 윈도우가 있는거지. 왼쪽이 점점 늘어나고
오른쪽이 점점 줄어드는 방식으로 전진? 하는거. 

아래 솔루션 다시 돌리면 Time exceed 발생함.
틀린 솔루션임. 정답뜰때 있고 오답뜰때 있음 -> 이렇게 푸는게 아님. 
''' 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1 


'''
Runtime: 247 ms, faster than 29.83% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.3 MB, less than 50.77% of Python3 online submissions for Find Pivot Index.

정답 솔루션: 
경계범위를 제대로 잡아주고 풀면 금방 풀림.
pivot 이 어디부터 어디까지 도는지 for 문으로 잡아주고 내부에서 pivot +1 로 돌때
범위 넘어가는지만 체크해주면 풀림.  
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 
        if len(nums) == 2:
            if nums[0] == 0:
                return 1
            if nums[1] == 0:
                return 0 

        # 초기 조건은 피봇이 0인 상황 
        left_sum = 0
        right_sum = sum(nums[1:])
        for pivot in range(0, len(nums)):
            if left_sum == right_sum:
                return pivot
            else:
                left_sum += nums[pivot]
                if pivot+1 < len(nums):
                    right_sum -= nums[pivot+1]
    
        return -1 
    
'''
개선 솔루션:
total_sum - left_sum - nums[i] === left_sum
위 방식대로 풀면 더 빠를듯? 
'''







