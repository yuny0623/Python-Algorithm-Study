'''
1006 
'''

a = input().rstrip()
b = input().rstrip() 

c = [] 

for i in range(8):
    c.append(int(a[i]))
    c.append(int(b[i]))

while len(c) > 2: 
    temp = [] 
    for i in range(len(c) - 1):
        n = (c[i] + c[i + 1]) % 10 
        temp.append(n)
    c = temp 

print(str(c[0])+str(c[1]))

