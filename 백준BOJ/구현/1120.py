'''
0747
https://www.acmicpc.net/problem/1120

두 문자열 주어짐. 같은 인덱스에서 같지 않은 문자의 개수 

a의 길이는 b보다 작거나 같다. 
a가 b와 같아질때까지 아래 연산이 가능하다. 
.. 
A의 앞에 아무 알파벳이나 추가한다.
A의 뒤에 아무 알파벳이나 추가한다.

이떄 길이는 같게 근데 a와 b의 차이는 최소로 하는걸 만들어라. 
'''
def compare_same_size_string(a, b):
    diff = 0 
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1 
    return diff 

A, B = input().split() 

if len(A) == len(B):
    diff = compare_same_size_string(A, B)
    print(diff) 
else: 
    diff = 0
    li = [] 
    for i in range(len(B) - len(A) + 1):
        for j in range(len(A)):
            if A[j] != B[i + j]:
                diff += 1
        li.append(diff)
        diff = 0   
    print(min(li))