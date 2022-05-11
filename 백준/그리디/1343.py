'''

1022 
~
1055 
'''

board = list(input().rstrip())

i = 0
l = len(board)

result = [] 

flag = True

while i < l:
    count = 0 
    if board[i] == '.':
        i += 1
        result.append('.')
        continue 
    elif board[i] == 'X':
        while i<l and board[i] != '.':
            i += 1
            count += 1

    if count %2 != 0: # 홀수는 보드판 생성 불가능.
        print("-1")
        flag = False
        break 
    else:             # 짝수라면? 
        if count % 4 == 0:
            for j in range(count//4):
                result.append('AAAA')
        else:
            for k in range(count//4):
                result.append('AAAA')
            result.append('BB')

if flag:
    print("".join(result))

    


