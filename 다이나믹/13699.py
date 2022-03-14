'''
1034
'''

n = int(input())

d = [0] * (35 + 1)
d[0] = 1
d[1] = 1
for i in range(2, n + 1):
    for j in range(i): # i = 2번 j- > 0 1 
        d[i] += d[j]*d[i-j-1] # d[2] += d[0]*d[2-0] / d[2] = d[1]*d[2-1-1]
print(d[n])