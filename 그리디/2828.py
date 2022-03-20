'''
1120 
~
1153 
'''

import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
j = int(input())

apple = [] 
for _ in range(j):
    apple.append(int(input()))

start = 1
end = m 

count = 0 
for a in apple:
    if a < start:
        count += start - a
        start = a
        end =  a + m - 1
    if a > end:
        count += a - end
        start = a - m + 1
        end = a

print(count)