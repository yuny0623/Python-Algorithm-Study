import sys
from typing import List 
'''
0820 ~ 
문제 자체는 쉬운데 시간복잡도 조건때문에 
고민해봐야할 문제.  + 나올 수 있는 값 범위가 음수까지 있어서
계수정렬도 쓰기 애매한 문제임. 
'''

# 1 번 솔루션 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        check = []
        for n in nums:
            if n not in check:
                check.append(n)
            else:
                check.remove(n)
        
        return check[0]
            
'''
1번 솔루션 조금 느리지? 딱봐도 느려보임. 
xor을 이용한 방법이 있음. 이게 훨씬 빠름. 
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer = answer ^ i
        return answer
