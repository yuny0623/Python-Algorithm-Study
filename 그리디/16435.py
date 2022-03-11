import sys
input = sys.stdin.readline
N, L = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort() # 정렬하기 
tall = L

for h in fruit:
    if tall < h:
        break
    tall += 1

print(tall)
