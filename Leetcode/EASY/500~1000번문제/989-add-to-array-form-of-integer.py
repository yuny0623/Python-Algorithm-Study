'''
1152 ~ 1159 

Runtime: 534 ms, faster than 26.03% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15 MB, less than 51.38% of Python3 online submissions for Add to Array-Form of Integer.

코멘트:
구현문제임. 참고로 map 은 적용했을때 list 를 리턴하지 않는다. map object 를 리턴한다. 
그러니 반드시 map 적용하고 나면 list 로 형변환해야 결과 제대로 나온다. 
'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, num))) + k))))

