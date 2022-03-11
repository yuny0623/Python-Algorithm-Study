N, M = map(int, input().split()) 
if N == 1: 
    scount = 1 
elif N == 2: 
    scount = min(4, (M-1)//2 + 1) 
elif M < 7: 
    scount = min(4, M) 
else: 
    scount = (2 + (M-5)) + 1 
print(scount)

'''
https://it-college-diary.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1783%EB%B2%88-%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8
'''
'''
솔루션
체스판의 세로가 3보다 작거나 7보다 작은 경우를 1) N이 1인 경우, 2) N이 2인 경우 3) N>=3, M <7인 경우로 분할한다.

1) N이 1인 경우

위아래로 한 칸도 움직일 수 없으므로 현재 나이트가 존재하는 칸 외 이동 가능한 칸이 없다. 따라서 scount = 1

2) N이 2인 경우

위아래로 한 칸씩 움직일 수 있다. 따라서 가로로 2칸씩 몇 번 이동할 수 있는지 계산해보면 M에서 현재 있는 1을 제외한 후 2로 나눈 값만큼 이동이 가능하다. 이동 가능 횟수는 최대 3번(4번 이상 이동 시 4가지 이동 방법을 모두 사용해야 하기 때문)이므로 이동 가능 횟수는 3과 (M-1)//2 중 작은 값이 된다. 나이트가 방문한 칸 수 = 이동 가능 횟수 + 1이므로 나이트가 방문한 칸 수는 4와 (M-1)//2+1 중 작은 값과 같다. (나이트가 방문한 칸 수 = 이동 가능 횟수 +1인 이유는 이동하면서 오른쪽으로 무조건 한 칸 이상 움직여야 하므로 여행 중 동일한 칸을 중복하여 방문할 수는 없기 때문이다. 따라서 첫 번째 칸과 이동 중 방문한 칸(=이동 횟수)을 더한 값과 나이트가 방문한 칸 수는 동일하다.)

3) N >=3 , M <7인 경우

N이 3과 같거나 3보다 크기 때문에 세로로는 위, 아래 두 칸씩 이동이 가능하므로 최대로 이동하기 위해서는 오른쪽으로 한 칸씩만 이동한다. 오른쪽으로 한 칸씩 이동하는 경우 최대 이동 횟수는 M-1이다. 하지만 최대 이동 횟수는 3보다 큰 값을 가질 수 없다. (4번 이상 이동 시 4가지 이동 방법을 모두 사용해야 하기 때문) 따라서 이동 가능 횟수는 3과 M-1 중 작은 값과 같으며 방문한 칸 수는 4와 M 중 작은 값과 같다.

4) N이 3보다 크거나 같고, M이 7보다 크거나 같은 경우

2칸 위로, 1칸 오른쪽

1칸 위로, 2칸 오른쪽

1칸 아래로, 2칸 오른쪽

2칸 아래로, 1칸 오른쪽

N이 3보다 크거나 같다면 위, 아래로 이동할 수 있기 때문에 이동 경로에 영향을 주지 않게 된다. 하지만 나이트가 오른쪽으로만 이동하기 때문에 4가지 이동 방법 중 1,4번의 이동을 반복하는 것이 최대 이동 횟수를 만들기에 유리하다. 하지만 2,3번 이동 또한 한 번은 이루어져야 하기 때문에 이동 횟수는 (2(2,3번 이동 1회씩)+(M-5)(M에서 나이트가 처음 있던 한 칸과 2,3번 이동으로 인한 4칸을 뺀 값))이며 최대 방문 가능한 칸 수는 이동 횟수 +1이다.



출처: https://it-college-diary.tistory.com/entry/그리디-알고리즘-백준-1783번-병든-나이트 [CodeLog]
'''