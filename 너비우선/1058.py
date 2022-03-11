# 0943 
N = int(input())
v = [[0]*N for _ in range(N)]

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if g[i][j] == 'Y' or (g[i][k] == 'Y' and g[k][j] == 'Y'): 
                    v[i][j] = 1

g = []
for _ in range(N):
    g.append(list(input()))

floyd()

result = 0
for i in range(N):
    count = 0
    for j in range(N):
        if v[i][j] == 1:
            count += 1
    result = max(result, count)

print(result)

'''
https://pacific-ocean.tistory.com/301
'''