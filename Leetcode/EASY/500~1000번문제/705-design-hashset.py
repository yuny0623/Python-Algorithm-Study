'''
0336 ~ 0340

Runtime: 317 ms, faster than 43.76% of Python3 online submissions for Design HashSet.
Memory Usage: 18.9 MB, less than 67.15% of Python3 online submissions for Design HashSet.

코멘트:
재밌는 문제. 참고로 set는 append는 쓰는게 아니라 add 를 쓴다. 
'''

class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)