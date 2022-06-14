'''
'''

n = int(input())

for i in range(n):
    a= int(input())
    li = list(map(int, input().split()))
    result = 0 
    if len(li) == 1:
        print("0")
        continue
    if li == sorted(li, reverse = True):
        print("-1")
        continue

    for i in range(len(li) - 1, 0, -1):
        if li[i] <= li[i - 1]:
            while li[i] != 0 and li[i] <= li[i - 1]:
                li[i - 1] = li[i - 1] // 2
                result += 1

    if sorted(li) != sorted(list(set(li))):
        print("-1")

    print(result)
