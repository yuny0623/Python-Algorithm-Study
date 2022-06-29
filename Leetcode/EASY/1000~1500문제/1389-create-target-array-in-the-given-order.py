'''
0434 ~ 0436 

Runtime: 43 ms, faster than 71.61% of Python3 online submissions for Create Target Array in the Given Order.
Memory Usage: 13.9 MB, less than 13.41% of Python3 online submissions for Create Target Array in the Given Order.


코멘트:
insert 는 동적으로 list 가 늘어날 수 있음. 그래서 미리 target 사이즈를 잡아줄 필요가 없음. 
그냥 빈 리스트로 잡고 시작해도 됨. 
'''

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # 0434 ~ 0436 
        # 그냥 insert 쓰면 끝남. 
        # insert 를 할 경우 list 크기가 동적으로 늘어남. 그래서 초기에 target list 크기를 미리 지정해줄 
        # 필요가 없음. 
        target = []
        i = 0 
        for idx in index:
            target.insert(idx, nums[i])
            i += 1
        
        return target 
        