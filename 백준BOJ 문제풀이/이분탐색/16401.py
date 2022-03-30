'''
0806 
과자 나눠주기 문제 
'''

import sys
input = sys.stdin.readline 

M, N = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0 

while start <= end:
    total = 0
    mid = (start + end ) // 2

    if mid == 0:
        total = 0
        break

    for a in array:
        if a >= mid: 
            total += (a // mid)

    if total >= M: 
        result = mid 
        start = mid + 1

    else:
        end = mid - 1

print(result)















