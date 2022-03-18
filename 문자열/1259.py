'''
1147 
'''

import sys
input = sys.stdin.readline 

while True:
    n = list(input().rstrip())
    if len(n) == 1 and n[0] == '0':
        break

    flag = False 
    for i in range(len(n)//2): 
        if n[i] == n[len(n) - i - 1]:
            continue 
        else:
            print("no")
            flag = True
            break 

    if flag == False:
        print("yes")

    


