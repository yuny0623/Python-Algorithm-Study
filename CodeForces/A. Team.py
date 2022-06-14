'''
0201 ~ 0203 

코멘트:
쉬워용 
'''
n = int(input())

solve = 0 
for i in range(n):
    li = list(map(int, input().split())) 
    count = 0
    for n in li:
        if n == 1:
          count += 1
    if count >= 2:
        solve += 1

print(solve)  