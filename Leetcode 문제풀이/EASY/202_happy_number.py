'''
1222  ~ 0156 
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        start = list(str(n))
        happy = False 
        is_cycle = [] 
        while True: 
            hap = 0
            for i in range(len(start)):
                hap += int(int(start[i]) ** 2)
                
            start = list(str(hap))
            
            if hap in is_cycle:
                happy = False
                break 
            
            is_cycle.append(hap)
                
            if hap == 1:
                happy = True
                break 
                
        print(is_cycle)
        return happy 
            
# # 2 4 16 1 36 = 37 9 49 = 58 25 64 = 89 64 81 = 125 1 4 25 = 30 9 0 = 9 81 1 64 = 65 
# 36 25 = 61 36 1 = 37 9 49 

# 19 , 1 81 = 82, 64 4 = 68, 36 64 = 100, 1  

