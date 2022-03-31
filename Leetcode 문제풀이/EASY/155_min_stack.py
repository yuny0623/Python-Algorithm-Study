'''
0943 ~ 0945 
'''

class MinStack:

    def __init__(self):
        self.list = [] 

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        self.list.pop()        

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
다른 사람 코드 
'''
class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)
        return None
