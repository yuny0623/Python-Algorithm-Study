'''
0812 ~ <답지보고 풀음 > ~ 

코멘트: 
ㅋ큐큐 
'''

'''
오답 솔루션: 

히든케이스에서 걸려 흑 
'''
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool: 
        points = sorted(points)
        last_point = points[-1][0]
        
        for i in range(1, 3):
            if points[i - 1] == points[i]:
                return False 
        
        count1 = 0
        for i in range(1, 3):
            if points[i - 1][0] == points[i][0]:
                count1 += 1
        if count1 >=2:
            return False 
        
        count2 = 0
        for i in range(1, 3):
            if points[i - 1][1] == points[i][1]:
                count2 += 1
        if count2 >=2:
            return False 
        
        count = 0 
        for i in range(1, last_point + 1):
            if points[0] == [i, i]:
                count += 1
            if points[1] == [i, i]:
                count += 1
            
        if count >= 2:
            return False
        return True 

'''
정답 솔루션: <답지 보고 풀음>
Runtime: 46 ms, faster than 53.28% of Python3 online submissions for Valid Boomerang.
Memory Usage: 13.9 MB, less than 62.30% of Python3 online submissions for Valid Boomerang.

기울기까지 비교해주고 있다. 위 솔루션에서는 기울기 비교해주는걸 안했다. 
아래 예제가 배울게 많다. 특히 zip 사용법도 그렇고, 
'''

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool: 
        x_points = list(set(list(zip(*points))[0]))
        y_points = list(set(list(zip(*points))[1]))
        
        if len(set(map(tuple, points))) != 3: return False 
        if len(x_points) == 1: return False
        if len(y_points) == 1: return False 
        if len(x_points) ==2 or len(y_points) == 2: return True 
        
        slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])  
        slope2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        
        return False if slope1 == slope2 else True 


