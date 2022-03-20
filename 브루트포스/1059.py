'''
1015 
'''
import sys
input = sys.stdin.readline 

L = int(input())
array = list(map(int, input().split()))
n = int(input())
array.sort() 

start = 0
end = 0

for i in range(len(array)):
    if n < array[i]:
        start = i - 1
        break
for i in range(len(array)):
    if n > array[i]:
        end = i 




