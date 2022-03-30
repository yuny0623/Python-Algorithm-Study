'''
0118 
~ 
0153 
'''

s = list(map(int, input()))

i = 0
count_0 = 0
while i <len(s): # 1을 뒤집어서 모두 0으로 만들자. 
    if s[i] == 0:
        i += 1
    else: 
        while i < len(s) and s[i] != 0:
            i += 1
        count_0 += 1

i = 0
count_1 = 0
while i < len(s): # 1을 뒤집어서 모두 0으로 만들자. 
    if s[i] == 1:
        i += 1
    else: 
        while i < len(s)  and s[i] != 1:
            i += 1
        count_1 += 1

print(min(count_0 , count_1))