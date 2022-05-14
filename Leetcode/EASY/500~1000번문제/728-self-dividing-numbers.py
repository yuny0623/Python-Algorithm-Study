'''
0535 ~ 0540

Runtime: 53 ms, faster than 79.94% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 13.9 MB, less than 24.01% of Python3 online submissions for Self Dividing Numbers.

코멘트:
쉬운문제. 문제 그대로 구현하면 됨. 
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            is_divide = True
            if '0' in str(num):
                continue
            for c in str(num):
                if num%int(c) != 0:
                    is_divide = False
            if is_divide:
                result.append(num)
                
        return result 


