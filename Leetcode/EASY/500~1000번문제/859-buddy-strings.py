'''
1150 ~ <답지 보고 풀음.>

코멘트:
생각보다 예외 케이스가 많음. 
예외만 주의하면 쉽게 풀 수 있음. 
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
        
        swap_pos = []
        i = 0 
        for a, b in zip(s, goal):
            if a != b:
                swap_pos.append(i)
            i += 1
        
        s = list(s[:])
        goal = list(goal[:])
        
        if len(swap_pos) == 2:
            s[swap_pos[0]], s[swap_pos[1]] = s[swap_pos[1]], s[swap_pos[0]]
            return s == goal 
        else:
            if len(set(s)) == 1:
                return True
            return False 