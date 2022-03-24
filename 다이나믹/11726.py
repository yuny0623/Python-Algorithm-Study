'''
1030
'''
n = int(input())

d = [0] * 1002 # 1001 번째까지 가능하도록! 
d[1] = 1
for i in range(2, 1002):
    d[i] = (d[i - 1] + d[i - 2])%10007
print(d[n + 1])