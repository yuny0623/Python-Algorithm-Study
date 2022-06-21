'''
1009 ~ <답지보고 풀음 >

코멘트: 생각보다 안풀림. 
특히 반시계방향으로 뒤돌아가는게 안풀림. 
'''

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 좋은 문제다. 
        clockwise_cost = 0  
        counterclockwise_cost = 0  
        
        i = start 
        while i != destination:
            if i >= len(distance):
                i = 0
            clockwise_cost += distance[i]
            if i == destination:
                break 
            i += 1
            
        j = start - 1
        if j <= -1:
            j = len(distance) - 1
        while j != destination:
            if j <= -1:
                j = len(distance) - 1
            counterclockwise_cost += distance[j]
            if j == destination:
                break 
            j -= 1
        counterclockwise_cost+= distance[j]

    
        print("clockwise_cost:{0}".format(clockwise_cost))
        print("counterclockwise_cost:{0}".format(counterclockwise_cost))
        return min(clockwise_cost, counterclockwise_cost)

'''
답지보고 푼 솔루션: 

Runtime: 60 ms, faster than 65.30% of Python3 online submissions for Distance Between Bus Stops.
Memory Usage: 15 MB, less than 8.45% of Python3 online submissions for Distance Between Bus Stops.
'''

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start 
        return min(sum(distance[start:destination]), sum(distance) - sum(distance[start:destination]))



