'''
0724 ~ 0729 
Runtime: 71 ms, faster than 5.24% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 13.8 MB, less than 59.72% of Python3 online submissions for Student Attendance Record I.

생각보다 속도가 느리게 나왔음. count 로 개수세주는거랑 in 으로 탐색해주는것때문에 그런것같음. 
''' 
class Solution:
    def checkRecord(self, s: str) -> bool:
        # 전체에서 이틀이상 결석하면 안됌. 
        # 3일 혹은 그 이상 연속된 날짜만큼 지각하면 안됨. 
        if s.count('A') >= 2:
            return False
        if 'LLL' in s:
            return False
        return True 
            

'''
새로운 솔루션1: 
Runtime: 69 ms, faster than 5.24% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 13.8 MB, less than 96.73% of Python3 online submissions for Student Attendance Record I.

위 코드보다 빠를줄 알았는데 거의 차이 안남. 
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        l = len(s)
        i = 0
        count_A = 0
        count_L = 0
        while i < l:
            if s[i] == 'A':
                count_A += 1
            if count_A == 2:
                return False 
            if s[i] == 'L':
                if i+2 < l and s[i:i+3] == 'LLL':
                    return False
            i += 1
        return True 
        
'''
개선한 솔루션2: 
20퍼센트까지 올림 
실행하기 전에 먼저 결석 2번 이상한애들 걸러주고 시작하면 조금 빠르게 시작할 수 있음. 
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False 
        l = len(s)
        i = 0
        count_A = 0
        count_L = 0
        while i < l:
            if s[i] == 'A':
                count_A += 1
            if count_A == 2:
                return False 
            if s[i] == 'L':
                if i+2 < l and s[i:i+3] == 'LLL':
                    return False
            i += 1
        return True 
        
'''
~ 0737 
개선한 솔루션3:
27퍼센트까지 올림 

Runtime: 51 ms, faster than 27.33% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 13.7 MB, less than 99.81% of Python3 online submissions for Student Attendance Record I.
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        # 전체에서 이틀이상 결석하면 안됌. 
        # 3일 혹은 그 이상 연속된 날짜만큼 지각하면 안됨. 
        if s.count('A') >= 2:
            return False 
        l = len(s)
        i = 0
        while i < l:
            if s[i] == 'L':
                if i+2 < l and s[i:i+3] == 'LLL':
                    return False
            i += 1
        return True 
        