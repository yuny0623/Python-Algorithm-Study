'''
0442 ~ 0601 <답지보고풀음>

코멘트: 
유난히 헤맨 문제. 너무 오래 걸렸음. 

유독 Wrong answer 와 Time limit이 남발한다면 접근법은 맞는데 
아예 구현 방법이 틀렸을 수 있다. 이 문제가 그런 경우다. 

슬라이딩 윈도우처럼 계산하는것까지는 떠올렸다. 근데 여기까지 떠올렸는데 
Time limit 이 뜬다? 이건 슬라이딩 윈도우를 제대로 활용하지 못해서 틀린거다.
아래 코드가 가장 효율적인 정답 코드이다. 

팁: 윈도우 내의 범위를 매번 sum 으로 새로 계산해줄 필요 없다. 
기본 base 초기값에서 한칸 전진한 뒷요소만큼 더해주고 한칸 전진한 만큼 앞요소값을 빼주면 된다. 
'''
import sys 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        best = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]  # 여기가 슬라이딩 윈도우의 활용이다. 
            best = max(best, s)
        
        return best/k 
            

'''
이전에 시도한 오답코드: 
'''
import sys 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # k 사이즈의 가장큰 subarray 를 찾으세요 
        # 부루트 포스 같은데? 슬라이딩 윈도우처럼 움직이면서 브루트 포스 서치 ㄱㄱ 
        if len(nums) == k:
            return sum(nums) / k
        if k == 1:
            return max(nums) / 1

        start = 0
        end = k - 1
        max_average = 0
        if sum(nums) < 0:
            max_average = -sys.maxsize
        # 음수인 경우 어떻게 하실? 
        while end < len(nums):
            s = sum(nums[start:end + 1])
            if (s / k) > max_average:
                max_average = s / k 
            start += 1
            end += 1

        return max_average 
            