# 0번째 피보나치 수는 0이다. 
# 0312 
# n = int(input())
# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# elif n == 2:
#     print(1)    
# else:
#     d = [0] * (n + 1)
#     d[1] = 1
#     d[2] = 1
#     for i in range(3, n + 1):
#         d[i] = d[i - 1] + d[i - 2]
#     print(d[n])

# 더 간단한 방법 
n = int(input())
s = [0, 1, 1]
for i in range(3, n + 1):
    s.append(s[i - 1] + s[i - 2])
print(s[n])