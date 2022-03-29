'''
0431 
~
0601 
((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100
'''

import sys
input = sys.stdin.readline 

def prob(L, O, V, E):
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100 

name = input().rstrip() 

# 이름의 개수 
l = 0
o = 0
v = 0 
e = 0

for c in name:
    if c == 'L':
        l += 1
    elif c == 'O':
        o += 1
    elif c == 'V':
        v += 1
    elif c == 'E':
        e += 1 

n = int(input())
count = [0 for _ in range(n)] 
team = [] 
for _ in range(n):
    team.append(input().rstrip())

for i in range(n):
    L = 0
    O = 0
    V = 0
    E = 0 
    for c in team[i]:
        if c == 'L':
            L += 1
        if c == 'O':
            O += 1
        if c == 'V':
            V += 1
        if c == 'E':
            E += 1 

    count[i] = prob(L +l, O +o, V + v, E + e) 

result = []
m = max(count)
for i in range(len(count)):
    if count[i] == m:
        result.append(team[i])

result.sort()

print(result[0])







