# 카이사르 
# 대문자 알파벳이 주어짐. 원래대로 바꾸세요 ~ 
# A = 65 
# Z = 90
from sys import stdin, stdout

w = input() 
new_w = ''
for i in range(len(w)):
    if ord(w[i]) - 3 >= ord('A'):
        new_w += (chr(ord(w[i]) - 3))
    elif ord(w[i]) - 3 < ord('A'): # x > 90 
        new_w+=(chr(90 - (ord('A') - (ord(w[i]) - 3)) + 1)) 
print(new_w)