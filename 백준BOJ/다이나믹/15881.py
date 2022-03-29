# 0855
#펜-파인애플-애플-펜
#p-P-A-p = pPAp
import sys
input = sys.stdin.readline
n = int(input())
str = input().rstrip()
word = "pPAp"

i = 0
count = 0
while i < n:
    if str[i] == word[0]:
        if str[i:i+4] == word: # len(word)지만 4로 써주었다. 
            count += 1
            i = i+3 # 사실은 i + len(word) - 1 이다. 
    i += 1

print(count)






