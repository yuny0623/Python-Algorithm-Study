'''
1158 
'''

import sys
input = sys.stdin.readline 

n = int(input())

student = [] 

for _ in range(n):
    student.append(list(map(int, input().split())))

candidate = [] # 임시 반장 후보군  
s_class = [0  for _ in range(10)] # 학급 
for i in range(5): # 5학년까지 돌게요 
    li = [] 
    for j in range(len(student)): 
        s_class[student[i][j]] += 1
    
    m = max(s_class)
    for k in range(len(student)):
        if student[i][k] == m:
            candidate.append(k)

print(max(candidate))       

    

