'''
0120 ~ 0134 
'''

n = int(input())

for i in range(n):
    word = input().rstrip()
    if len(word) <= 10:
        print(word)
        continue 
    else:
        new_word = word[0] + str(len(word) - 2) + word[-1]
        print(new_word)
        continue 



