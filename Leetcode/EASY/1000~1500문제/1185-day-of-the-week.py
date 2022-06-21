'''
1130 ~ <답지보고풀음>


'''


'''
오답 솔루션:
'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31] 
        day_string = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
        total_day = 0 
        for i in range(0, year):
            if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
                total_day += 1
            total_day += 365
        
        total_day += sum(month_days[:month]) # 8월 
        print(sum(month_days[:month]))
        print(day)
        total_day += day
        return day_string[total_day%7]
        # 결과: sunday 1
        # 정답: saturday 0  
            

'''
정답 솔루션 :
Runtime: 51 ms, faster than 32.86% of Python3 online submissions for Day of the Week.
Memory Usage: 13.9 MB, less than 75.54% of Python3 online submissions for Day of the Week.

근데 이거 datetime 쓰지 않고 그냥 연산해서 풀 수 있는 방법은 없을까? 

'''
import datetime 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_string = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
        week_day = datetime.datetime(year, month, day).weekday() 
        return day_string[week_day%7]
            

