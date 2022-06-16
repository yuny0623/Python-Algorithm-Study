'''
1131 ~ 1254 

Runtime: 8504 ms, faster than 5.03% of Python3 online submissions for Number of Recent Calls.
Memory Usage: 19.6 MB, less than 18.38% of Python3 online submissions for Number of Recent Calls.

코멘트: 
'''
'''
솔루션1: 
이건 정답은 맞는데 제대로된 솔루션인지는 의문이다. 7~8초 정도 걸리는데
이게 너무 오랜 시간이 걸린다. 그래서 아마 성능 개선이 가능할 것 같다. 해보자. 
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


'''
솔루션2:
일부 풀이 중에서 queue 쓰는 풀이가 몇개 있었다. 그래서 이걸 deque 쓰는걸로 바꾸었다. 
속도가 조금은 빨라졌다. 

Runtime: 4318 ms, faster than 8.43% of Python3 online submissions for Number of Recent Calls.
Memory Usage: 19.8 MB, less than 18.38% of Python3 online submissions for Number of Recent Calls.

그래도 아직도 느리다. 
'''
from collections import deque 
class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        start = t - 3000 
        if start < 0:
            start = 0 
    
        count = 0
        for i in range(len(self.counter)):
            if self.counter[0] < start:
                self.counter.popleft()
            
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)