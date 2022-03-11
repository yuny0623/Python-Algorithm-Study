# 0940 

import sys
s = sys.stdin.readline().rstrip()
i = 0
result = s[0]
while True:
    k = s.find("-", i + 1)
    i = k
    if k != -1:
        result += s[k+1]
    else:
        break
    
print(result)