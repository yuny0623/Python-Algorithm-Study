import sys
input = sys.stdin.readline

N = int(input())
tip = []
for _ in range(N):
    tip.append(int(input()))
tip.sort(reverse = True) #내림차순 정렬

result = 0
rank = 1 
for t in tip:
    if(t - (rank - 1) > 0):
        result += (t - (rank - 1))
    else:
        result += 0
    rank += 1

print(result)