'''
0615 
두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
'''

x, y = map(str, input().split())
x = x[::-1]
y = y[::-1]

z = str(int(x) + int(y))
z = z[::-1]

print(int(z))