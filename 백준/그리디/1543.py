# 0553
str = input()
word = input()

count = 0

i = 0
for _ in range(len(str)): # 9
    if str[i] == word[0]: # 첫글자가 같은걸 찾으면!
        if str[i:i+len(word)] == word: #012 str[0:3] -> 012
            count += 1
            i = i + len(word) - 1 # 다음 탐색 구간으로 이동  = 3
    i += 1
    if i >= len(str):
        break

print(count)