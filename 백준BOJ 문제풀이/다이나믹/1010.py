
'''
m이 n보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 n개이고
m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 때문에
mCn 으로 표현할 수 있고 이는 m! 을 (m-n)!n! 으로 나눈 값이 된다.
'''
import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)
    