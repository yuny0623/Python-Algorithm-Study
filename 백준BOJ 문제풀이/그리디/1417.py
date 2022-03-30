'''
1055
~
1117 
'''

import sys
input = sys.stdin.readline 

candidate = [] 
n = int(input())
for _ in range(n):
    candidate.append(int(input()))
if n == 1:
    print(0)
else:
    me = candidate[0]
    other = candidate[1:]

    count = 0 
    while True:
        if me > max(other):
            break 
        else:
            other.sort(reverse = True)
            other[0] -= 1
            me += 1
            count += 1

    print(count)



