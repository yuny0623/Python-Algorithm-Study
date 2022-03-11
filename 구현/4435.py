# 간달프 1 2 3 3 4 10 
# 사우론 1 2 2 2 3 5 10 

from sys import stdin, stdout

T = int(input())

for i in range(T): 
    a = list(map(int, stdin.readline().split())) # 간달프  
    b = list(map(int, stdin.readline().split())) # 사우론 

    A = a[0] + a[1] * 2 + a[2] * 3 + a[3] * 3 + a[4] * 4 + a[5] * 10
    B = b[0] + b[1] * 2 + b[2] * 2 + b[3] * 2 + b[4] * 3 + b[5] * 5 + b[6] * 10
 
    if A > B:
        print("Battle {0}: Good triumphs over Evil".format(i+1))
    elif A < B:
        print("Battle {0}: Evil eradicates all trace of Good".format(i+1))
    elif A == B:
        print("Battle {0}: No victor on this battle field".format(i+1))

