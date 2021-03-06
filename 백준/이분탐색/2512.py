# 1104 
'''
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. 
N은 3 이상 10,000 이하이다. 
다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 
이 값들은 모두 1 이상 100,000 이하이다. 
그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 
'''
import sys
input = sys.stdin.readline

N = int(input())
bu = list(map(int, input().split()))
M = int(input()) 


if sum(bu) <= M: #상한액 필요없이 다 줄 수 있다면  
    print(max(bu)) #가장 큰 배정 예산액 출력 
else: 
    start = 1
    end = max(bu)
    mid = 0

    while start <= end:
        mid = (start + end)//2
        result = 0
        for a in bu:
            if a < mid : # 상한액보다 작으면 
                result += a # 그대로 더해준다. 
            else:         # 상한액보다 크면          
                result += mid  #상한액을 더해준다. 

        if result > M: # 예산보다 크면 ! 
            end = mid - 1 # 상한액을 줄인다.  
        elif result <= M: # 예산보다 작으면   
            start = mid + 1 #상한액을 늘린다.
        
    print(end)

'''
재밌는 문제다. 
  if result >= M: # 예산보다 크면 ! 
    end = mid - 1 # 상한액을 줄인다.  
  elif result < M: # 예산보다 작으면   
    start = mid + 1 #상한액을 늘린다.
첫번째 코드를 실행하면 틀리지만 
  if result = M: # 예산보다 크면 ! 
    end = mid - 1 # 상한액을 줄인다.  
  elif result <= M: # 예산보다 작으면   
    start = mid + 1 #상한액을 늘린다.
두번째 코드를 실행하면 정답처리된다. 

왜일까? 
문제의 조건은 다음과 같다. 
 " 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.  " 
즉 이말은 다 나눠줄 수 있는 예산액이면 가장 요구하는 예산이 큰 친구를 출력해주고
예산이 부족해서 상한액을 산정해서 나눠줘야 할 상황이면 그냥 상한액을 출력해달라는 말로 봐도 된다. 

그러므로 만약 상한액을 산정해야 한다면 상한액을 크게끔 만들어야 한다는 소리다. 
그러므로 elif result <= M: # 예산보다 작으면 ---> 즉 작을때는 무조건 
start 가 mid+1로 가는게 맞고, 만약 같다면? 그때도 더 큰 상한액을 구하기 위해 진행해야 하므로
같을 때도 mid +1로 늘려가는게 맞다. 

if result >= M: #  첫번째 코드에서 왜 이부분은 하면 안되냐? 라고 할 수 있는데, 
이 코드는 end = mid - 1 이다. 즉 오히려 범위를 줄인다.
즉 예산이 같아지는, 만족시키는 순간에조차 오히려 범위를 줄여버린다. 

그러므로 상식적으로 생각했을때, 맞지 않는 코드이다. 
'''
