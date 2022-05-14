'''
0345 ~ 0349 

Runtime: 293 ms, faster than 68.86% of Python3 online submissions for Design HashMap.
Memory Usage: 17.1 MB, less than 81.44% of Python3 online submissions for Design HashMap.

코멘트: 
코멘트할 내용이 없다. 재밌는 문제임. 
'''
class MyHashMap:

    def __init__(self):
        self.map = dict()

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

