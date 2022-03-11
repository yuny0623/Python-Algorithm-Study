# 0955
import sys
K, N = map(int, input().split())
# 오영식이 가지고있는 랜선 개수 K
# 필요한 랜선의 개수 N 
line_list = [int(sys.stdin.readline()) for _ in range(K)]

start = 1              # 최소값 즉 시작위치 # 얘는 요소중 가장 작은 값이 아니라 그냥 0부터 시작해야 한다. 
end = sum(line_list)//N   # 최대값 즉 끝 위치 
ans = 0
while start <= end:
    count = 0
    mid = (start + end) // 2  # mid는 이제 자르는 길이가 된다. 
    for a in line_list:
        count += a//mid
    if count < N:       # 너무 크게 자른거다. -> 개수가 부족함. 
        end = mid - 1     # 더 작게 자르도록 변경 
    elif count >= N:       # 너무 잘게 자른거다. -> 개수가 너무 많음. 
        start = mid + 1     # 크게 자르도록 변경
        ans = mid 

print(ans)
