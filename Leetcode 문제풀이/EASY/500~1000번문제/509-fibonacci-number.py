'''
0720 ~ 0726 

Runtime: 39 ms, faster than 67.82% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 56.57% of Python3 online submissions for Fibonacci Number.

개선할점:
global d 말고 다른 방법 없어? 좀 찝찝함. 
'''
global d 
d = [0] * 31
d[1] = 1
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if d[n] != 0:
            return d[n]
        d[n] = self.fib(n - 1) + self.fib(n - 2)
        return d[n]

'''
이거 변수 세개 써서 진행하는걸로 바꿔보자.-> 추가 메모리 사용없는걸로. 
'''
