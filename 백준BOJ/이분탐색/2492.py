# 1242  
from sys import stdin
from math import ceil # 천장 함수를 사용한 것이 핵심이다. 

def answer():
  global n, m, arr
  start, end, ans = (1, max(arr), 0)
  while(start <= end):
    mid, sections = ((start+end)//2, 0)
    for i in arr:
      sections += ceil(i/mid)
    if sections <= n: ans, end = (mid, mid-1)
    else: start = mid+1
  print(ans)

n, m = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(m)]

answer()
# https://develoger.kr/2792%EB%B2%88-%EB%B3%B4%EC%84%9D%EC%83%81%EC%9E%90/#









