'''
0743 ~ 0747 

Runtime: 103 ms, faster than 59.81% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.7 MB, less than 17.48% of Python3 online submissions for Sort Array By Parity.

코멘트: 
구현 문제. 그대로 구현하면 됨. 
참고로 extend 함수는 아무것도 리턴하지 않음. 그러므로 return even.extend(odd) 라고 쓰면 오답임.
왜냐. even 에는 반영되는데 extend 에서 even 을 리턴하지 않기 때문이다. 
근데 이거 추가 메모리 안쓰고 제자리에서 풀수 있나? -> 두개씩 잡아서 switch 하면 될것같은데... 해봅시다. 
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        even = []
        odd = []
        for n in nums:
            if n%2 == 0:
                even.append(n)
            else:
                odd.append(n)

        even.extend(odd)
        return even


'''
추가 메모리 사용안하는 제자리 정렬 솔루션: 

Runtime: 105 ms, faster than 57.51% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.8 MB, less than 17.48% of Python3 online submissions for Sort Array By Parity.

속도 차이는 크게 없네요. 
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
   
        start = 0
        end = len(nums) - 1
        print(nums)
        while start < end:
            if nums[start]%2 == 0:
                start += 1
                continue
            if nums[end]%2 == 1:
                end -= 1
                continue
            nums[start], nums[end] = nums[end], nums[start]
        print(nums)
        return nums