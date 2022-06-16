'''
1131 ~ 1254 

Runtime: 8504 ms, faster than 5.03% of Python3 online submissions for Number of Recent Calls.
Memory Usage: 19.6 MB, less than 18.38% of Python3 online submissions for Number of Recent Calls.

코멘트: 
이건 정답은 맞는데 제대로된 솔루션인지는 의문이다. 7~8초 정도 걸리는데
이게 너무 오랜 시간이 걸린다. 
'''

class RecentCounter:

    def __init__(self):
        self.counter = [] 

    def ping(self, t: int) -> int:
        self.counter.append(t)
        start = t - 3000 
        if start < 0:
            start = 0 
    
        count = 0
        for i in range(len(self.counter)-1, -1, -1):
            if self.counter[i] < start:
                break 
            count += 1
            
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


