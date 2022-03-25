'''
1112 
~
1219 
'''

import sys
input = sys.stdin.readline 

s = input().rstrip()
result = [] 
l = len(s)
i = 0 
while True:
    if i >= l:
        break 

    if s[i] == '<':
        tmp = ''
        while i < l and s[i] != '>':
            tmp += s[i]
            i += 1
        if i < l:
            tmp += '>'
            result.append(tmp)
            i += 1
            continue
        else:
            result.append(tmp)
            break  
    else:
        tmp = ''
        while i < l and s[i] != '<':
            if s[i] == ' ':
                result.append(tmp[::-1])
                result.append(s[i])
                i += 1
                tmp = ''
                continue 
            else: 
                tmp += s[i]
                i += 1
        result.append(tmp[::-1])

print(''.join(result))
