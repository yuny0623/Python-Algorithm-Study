'''
0819 

최소 부분합 문제 
'''

n = input()
numbers = list(map(int, input().split()))
max_num = max(numbers)
sum_num = sum(numbers)
print(sum_num-max_num)

