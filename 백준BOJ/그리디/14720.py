'''
0617
맨 처음에는 딸기우유를 한 팩 마신다.
딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 

이 규칙대로만 마심. 
즉 0 1 2 순서대로만 마심. 
'''

N = int(input())
li = list(map(int, input().split()))
milk = 0 
for i in range(len(li)):  
    if li[i] == milk%3:
        milk+=1
print(milk)
    

