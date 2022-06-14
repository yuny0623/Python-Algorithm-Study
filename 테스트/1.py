
# a ->  dog
# b -> cat
# c -> universal food 

# x  -> 보유 dog 
# y  -> 보유 cat 
n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    if li[0] + li[1] + li[2]  < li[3] + li[4]:
        print("NO")
        continue
    else:
        if li[0] < li[3]: # 강아지 사료가 적다면 
            if li[0] + li[2] < li[3]:
                print("NO")
                continue
        if li[1] < li[4]:
            if li[1] + li[2] < li[4]:
                print("NO")
                continue
    print("YES")
    
    
    