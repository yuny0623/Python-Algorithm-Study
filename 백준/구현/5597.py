# 1번 ~ 30번 
from sys import stdin, stdout

c = [i for i in range(1, 31)]
miss = []
for _ in range(28):
    n = int(stdin.readline())
    if n in c:
        c.remove(n)
        continue
    
c.sort()
print(c[0])
print(c[1])

