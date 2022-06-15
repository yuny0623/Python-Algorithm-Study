'''
1056 ~ 1119 

Runtime: 261 ms, faster than 54.52% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.4 MB, less than 45.17% of Python3 online submissions for Largest Perimeter Triangle.

코멘트: 
nums 가 길이가 3이상으로 올 수 있다는거에 주의. 
세개의 변 길이가 서로 어떤 관계에 있는지 생각해보면서 풀면 쉽게 풀림.
세 변중 가장 긴 변은 나머지 두개의 변의 합보다는 작아야한다.
또한 largest preimeter 즉 가장 긴 둘레를 구하라고 했으니 정렬한 다음 뒤에서부터 접근하는게 빠를거다. 
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)-1, 1, -1):
            print(nums[i-2], nums[i-1], nums[i]) # 2 2 3 
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i-2]+nums[i-1]+nums[i]
        return 0 

            

