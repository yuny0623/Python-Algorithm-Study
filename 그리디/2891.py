'''
1257 
'''

import sys
input = sys.stdin.readline 

# 팀의 수 n
# 카약이 손상된 팀의 수 s
# 카약을 하나 더 가져온 팀의 수 r 
n, s, r = map(int, input().split())

broken = list(map(str, input().split()))
surplus = list(map(str, input().split()))
print("broken: ", broken)
print("surplus: ", surplus)
broken.sort() 
for i in range(1, n + 1):
    if i == broken[0]:
        print("부서진팀번호:", broken[0])
        if i - 1 > 1 and (i - 1 in surplus):
            broken.pop(0)
            pos = surplus.find(i -1)
            surplus.pop(pos)
        elif i + 1 <= (n + 1) and (i + 1 in surplus):
            broken.pop(0)
            pos = surplus.find(i + 1)
            surplus.pop(pos)

print(len(broken))