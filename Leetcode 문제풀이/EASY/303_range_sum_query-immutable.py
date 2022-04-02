'''
0834  ~ 0839 
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums[:]

    def sumRange(self, left: int, right: int) -> int:
        if right > len(self.array) - 1:
            return None
        total = 0
        for i in range(left, right + 1):
            total += self.array[i]
        return total 
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)