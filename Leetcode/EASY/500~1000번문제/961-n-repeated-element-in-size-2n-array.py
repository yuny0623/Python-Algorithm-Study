'''
1015 ~ 1020 
Runtime: 298 ms, faster than 47.01% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.7 MB, less than 8.54% of Python3 online submissions for N-Repeated Element in Size 2N Array.
코멘트: 
중간에 굉장히 재미난 에러 동작이 있었는데 이건 파이썬 언어 차원에서의 문제인것 같다. 
굉장히 신기한게 지금 중간에 for문으로 nums에서 num으로 요소를 뽑으면서 d[num]을 1씩 증가시키는 코드가 있을 거다.
근데 이 num이라는걸 n으로 바꾸면? 결과는 None이 나온다. 즉 오답이 된다. 
for문 내부적으로 사용하는 변수인데 왜 이게 결과에 영향을 미칠까? 신기하네. 
아마 위에 선언한 n = len(nums)//2 변수가 할당된 location 을 아래 코드의 for문에서 n이 잡히면서 그 location을 
뒤집어씌우는 동작을 하는것 같다. 

그렇다면 해결 방법은? n = len(nums)//2 <- 이 코드를 for문보다 아래로 내리면 되겠지? 
근데 더 확실한건? for문이라해도 위에 선언된 변수와 겹치는 변수를 for 의 반복변수로 설정하지 말자는거다. 
이런 동작은 처음보는에 꽤나 생소하면서도 신기하다. 
 '''
from collections import defaultdict 
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 길이는 2의 배수 
        # n + 1개의 unique 한 요소 가지고 있음. 
        # 정확히 한개의 요소만 n번 반복해서 등장함. 
        n = len(nums)//2 
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for k, v in d.items():
            if v == n:
                return k 
