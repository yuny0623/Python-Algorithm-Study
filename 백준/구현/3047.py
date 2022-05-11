''' 0525
 세 수 A, B, C가 주어진다. A는 B보다 작고, B는 C보다 작다.
    a < b, b < c 
 세 수 A, B, C가 주어졌을 때, 입력에서 주어진 순서대로 출력하는 프로그램을 작성하시오.''' 

import sys
input = sys.stdin.readline

x, y, z =  map(int, input().split())
order = list(input().rstrip())
# A, B, C 
li = sorted([x, y, z])
dic = {'A': li[0], 'B': li[1], 'C': li[2]}

for c in order:
    print(dic[c], end=' ')


