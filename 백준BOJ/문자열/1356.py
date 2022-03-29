'''
0602 
~0613 
'''

n = list(input())

flag = False 
for i in range(1, len(n)):
    front = 1
    back = 1
    for j in range(len(n[:i])):
        front *= int(n[:i][j]) 
    for k in range(len(n[i:])):
        back *= int(n[i:][k])
    if front == back: 
        flag = True
        print("YES")
        break 

if not flag:
    print("NO")
     
    