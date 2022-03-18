'''

나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며,
마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로이다. 
'''

import sys
input = sys.stdin.readline 

arr = [input() for _ in range(36)]
if len(set(arr)) == 36:
    for i in range(35):
        if abs((ord(arr[i][0]) - ord(arr[i + 1][0])) * (int(arr[i][1]) - int(arr[i + 1][1]))) != 2:
            print("Invalid")
            sys.exit()

    i = 0
    for a, b in [[-2, -1],[-2, 1],[-1, -2],[1, -2],[2, -1],[2, 1],[1, 2],[-1, 2]]:
        i += 1 
        c = ord(arr[-1][0]) + a
        n = int(arr[-1][1]) + b
        if ord('A') <= c <= ord('Z') and 1<= n<= 6:
            if chr(c) == arr[0][0] and n == int(arr[0][1]):
                print("Valid")
                sys.exit()

    print("Invalid")
else:
    print("Invalid")