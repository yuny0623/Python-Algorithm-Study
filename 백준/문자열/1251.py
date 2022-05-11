# 0946 
# 첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다.

s = input()
m = "z"*len(s)

for i in range(0, len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            tmp = (s[:i + 1][::-1]) + (s[i + 1: j + 1][::-1]) + (s[j + 1: k + 1][::-1])
            m = min(tmp, m)
 
print(m)

