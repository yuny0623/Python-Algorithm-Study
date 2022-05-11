'''
    1043 
'''

n = int(input())

tmp1 = 0
tmp2 = 1
for i in range(n - 2 + 1):
    tmp1, tmp2 = tmp2 %  1000000007, (tmp1 + tmp2) %  1000000007
print(tmp2)