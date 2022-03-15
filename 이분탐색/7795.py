'''
0703 

 A가 B보다 큰 쌍의 개수를 출력한다.

 https://kau-algorithm.tistory.com/311?category=913229

'''
import sys
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    arrA.sort(reverse = True)
    arrB.sort(reverse = True) 

    count = 0
    a = 0
    b = 0
    while a < N and b < M: 
        if arrA[a] > arrB[b]:
            count += M - b 
            a += 1
        else: 
            b += 1

    print(count)

