'''
0310 ~ 0316

Runtime: 1584 ms, faster than 9.86% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.6 MB, less than 6.45% of Python3 online submissions for Kth Largest Element in a Stream.

코멘트: 
재미있는 문제. 쉬운 문제임. 
근데 매번 sorted하는게 좀 오버헤드가 되지 않을까요? 
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k
 # 10 9 8 5 5 4 3 2 
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse = True)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


'''
개선한 코드:
Runtime: 1013 ms, faster than 16.11% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.3 MB, less than 60.34% of Python3 online submissions for Kth Largest Element in a Stream.

이건 sort가 중복되지 않는다. 한번만 sort 하면 됨. 
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
 # 10 9 8 5 5 4 3 2 
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)