'''
0949 ~ 0953 

재밌는 문제다. 
딕셔너리를 활용하면 금방 풀 수 있음. 
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U':[-1,0], 'D':[1, 0], 'R':[0, 1], 'L':[0, -1]}
        origin = [0, 0]
        for m in moves:
            origin[0] += d[m][0]
            origin[1] += d[m][1]
        
        return origin == [0, 0]




