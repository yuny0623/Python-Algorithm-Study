'''

1141 
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
'''

N = list(map(int, input()))
count = [ 0 for i in range(10)]

for i in range(len(N)): 
    if N[i] in [6, 9]:
        count[6] += 1
    else:
        count[N[i]] += 1

if count[6] % 2 == 0:
    count[6] = count[6] // 2
else:
    count[6] = count[6] // 2 + 1

print(max(count))
