'''
1154 
'''

import sys
input = sys.stdin.readline 

# 현재 주파수 a
# 듣고 싶은 주파수 b 
a, b = map(int, input().split())
fix = []  # 고정 주파수 
n = int(input())
for _ in range(n):
    fix.append(int(input()))
fix.sort() 

pos = a 

if b in fix: 
    print("1")
else:   
    count_1 = abs(pos - b)
    count_2 = 0

    c_1 = 1001
    c_2 = 1001
    for i in range(len(fix)):
        if fix[i] > b:
            c_1 = fix[i] - b
            break
    for i in range(len(fix)):
        if fix[i] < b:
            c_2 = b - fix[i]
    count_2 = min(c_1 + 1, c_2 + 1)
        
    print(min(count_1, count_2))

