# 0501
import sys
input = sys.stdin.readline

ucpc = ['U','C','P','C']
str = input()
str = str.replace(' ', '')#공백제거
i = 0
for c in str:
    if c.isupper(): #대문자라면! 
        if c == ucpc[i]:
            i += 1
    if i == 4:
        break

if i >= 4:
    print("I love UCPC")
else:
    print("I hate UCPC")

