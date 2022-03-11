"""
헤일스톤 수열 
n이 짝수라면 2로 나눈다.
n이 홀수라면, 3을 곱한 뒤 1을 더한다. 

헤일스톤 추측 
임의의 양의 정수 n으로 수열을 시작한다면, 항상 4 2 1 4 2 1 로 끝난다는 추측이다. 여기서는 1이 나오면 수열 끝으로 판별함.

수열에서 가장 큰 값은 ?
"""
import sys 

T =  int(sys.stdin.readline())
for i in range(T):
    start = int(sys.stdin.readline())
    m = start  
    if start == 1:
        print(1)
        continue
    while start != 1:
        if start %2 == 0: # 짝수라면? 
            start //= 2
        else:
            start = start * 3
            start += 1
        m = max(m, start)
    sys.stdout.write(str(m) + "\n")

