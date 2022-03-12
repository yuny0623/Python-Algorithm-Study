'''
0550 

'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = input() 
    pelin = int(n) + int(n[::-1])
    if len(str(pelin)) == 1:
        print("YES")
    else:
        if str(pelin) != str(pelin)[::-1]:
            print("NO")
        else:
            print("YES")