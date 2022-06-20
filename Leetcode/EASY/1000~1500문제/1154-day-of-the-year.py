'''
1016 ~ 1029 

Runtime: 81 ms, faster than 87.91% of Python3 online submissions for Day of the Year.
Memory Usage: 13.8 MB, less than 98.06% of Python3 online submissions for Day of the Year.

코멘트: 
사실상 윤년 구하는 문제임. 
'''

class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 윤년계산 필요할듯 
        year = int(date[:4])
        month = int(date[5:7]) 
        day = int(date[-2:])
        num_of_year = sum(days[:month]) + day
        if (((year%4 == 0) and (year %100 != 0)) or (year%400 == 0)) and month >= 3:
            num_of_year += 1
        
        return num_of_year
        


