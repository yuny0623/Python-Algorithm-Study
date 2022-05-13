'''
0347 ~ 0354 

코멘트:
단순한 구현문제 
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for s in ops:
            if s not in '+DC':
                record.append(int(s))
            else:
                if s == '+':
                    record.append(record[-1] + record[-2])
                if s == 'D':
                    record.append(record[-1] * 2)
                if s == 'C':
                    record.pop()
        print(record)
        return sum(record)
    