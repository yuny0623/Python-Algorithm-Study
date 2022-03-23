
'''
1126

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.
'''

m = {*range(50001)}
a = {i*i for i in range(224)}
b = {i + j for i in a for j in a} & m
c = {i + j for i in a for j in b} & m
n = int(input())
print("a: ", a)
print()
print()
print("b: ", b)
print()
print()
print("c: ", c)

print(4 - (n in a) - (n in b) - (n in c))