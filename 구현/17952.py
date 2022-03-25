'''
0148 
~ 0234 -> 시간 초과 발생 ㄷㄷ 
~ 0303 -> 해결 
'''
import sys
input = sys.stdin.readline 

n = int(input())
total = 0 
stack = [] 
for _ in range(n):
    info = input().rstrip() 
    if info == '0':
        if stack: 
            score, time = stack.pop()
            time -= 1
            if time == 0: total += score
            else: stack.append([score, time]) 
    else:
        _, score, time = map(int, info.split(' '))
        time -= 1
        if time == 0: total += score
        else: stack.append([score, time])
    
print(total)