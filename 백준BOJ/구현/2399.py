import sys
import math 
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
dis = 0 
if len(li) == 1:
    print(dis)
else:
    for i in range(len(li)):
        for j in range(i, len(li)):
            dis += abs(li[i] - li[j])
    print(dis * 2)