'''
1056
'''

n = int(input())
result = [] 

for i in range(4, n + 1):
    flag = False
    for j in range(len(str(i))):
        if str(i)[j] == '4' or str(i)[j] == '7':
            flag = True
        else:
            flag = False
            break 

    if flag:
        result.append(i)    
    
print(max(result))

