'''
0745 ~ <답지보고 풀음>
답지: 
https://www.youtube.com/watch?v=_tfiTQNZCbs
'''

'''
오답 솔루션: 
division by zero 문제를어떻게 해
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates = sorted(coordinates, key = lambda x: (x[0], x[1]))
        print(coordinates)
        count = 0
        for i in range(1, len(coordinates)):
            if coordinates[i-1][0] != coordinates[i][0]:
                break
            count += 1
        if count == len(coordinates) - 1:
            return True 
        count = 0
        for i in range(1, len(coordinates)):
            if coordinates[i-1][1] != coordinates[i][1]:
                break
            count += 1
        if count == len(coordinates) - 1:
            return True 
        # 기울기만 같은지 확인하면 될듯 
        slope_x = coordinates[1][0] - coordinates[0][0] #
        slope_y = coordinates[1][1] - coordinates[0][1] #
        slope = 0
        if slope_x == 0:
            slope = 1
        elif slope_y == 0:
            slope = 1 
        else:
            slope = slope_y / slope_x
        #slope = slope_y * slope_x
        #print(slope)
        if len(coordinates) == 2:
            return True 
        for i in range(2, len(coordinates)):
            slope_x_i = coordinates[i][0] - coordinates[i - 1][0]
            slope_y_i = coordinates[i][1] - coordinates[i - 1][1]
            slope_i = 0
            if slope_x_i == 0:
                slope_i = 1
            elif slope_y_i == 0:
                slope_i = 1
            else:
                slope_i = slope_y_i / slope_x_i
            #print(slope_i)
            if slope != slope_i:
                return False 
        return True
    


'''
정답 솔루션: 수학문제였음. 
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            if ((coordinates[1][1] - coordinates[0][1])*(coordinates[i][0] - coordinates[0][0]) 
                != 
                (coordinates[1][0] - coordinates[0][0])*(coordinates[i][1] - coordinates[0][1])):
                return False 
        return True 
    