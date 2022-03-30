'''
1122 
'''

n = int(input())

d = [0 for i in range(n + 1)]

def dynamic(x):
    if x <= 1:
        return 0 
    if x == 2:
        return 1 
    if d[x] != 0:
        return d[x]
    d[x] = ((x//2) * (x - x//2)) + dynamic(x//2) + dynamic(x - (x//2))
    return d[x]

print(dynamic(n))


