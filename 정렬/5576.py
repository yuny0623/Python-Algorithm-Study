from sys import stdout, stdin

a = []
b = []
for _ in range(10):
    a.append(int(stdin.readline()))
for _ in range(10):
    b.append(int(stdin.readline()))

a.sort(reverse = True)
b.sort(reverse = True)
a = a[0] + a[1] + a[2]
b =  b[0] + b[1] + b[2]
print(a, b)

