#오후 4:42:23
import sys
input = sys.stdin.readline
N= int(input())
cow = [] 
for _ in range(N):
    cow.append(list(map(int, input().split())))

cow.sort() #정렬해주기 
result = 0

for i in range(0, N):
    if result <= cow[i][0]:
        result = sum(cow[i])
    else:
        result += cow[i][1]
    
print(result)


# 2 1 /   5 7 / 8 3
# 3
# 2 1
# 8 3
# 5 7

