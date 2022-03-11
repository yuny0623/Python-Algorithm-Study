# 0910
n1 = input()
n2 = input()
n3 = input()
iter = [n1,n2,n3]

for s in iter:
    count = 1 # 초기화 
    m = 1     # 초기화 

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            m = max(count, m)
        else:
            count = 1

    print(m)

'''
생각보다 고전한 문제다. 
'''