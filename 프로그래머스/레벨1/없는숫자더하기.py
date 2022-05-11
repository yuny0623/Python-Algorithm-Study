'''
0921 ~ 0922 

뭐지 왜 갑자기 쉬운 문제? 
'''

def solution(numbers):
    total = 0
    for i in range(10):
        if i not in numbers:
            total += i 
    return total 

'''
다른 사람 풀이를 구경하던 중 엄청난 코드를 발견...
'''
def solution(numbers):
    return 45 - sum(numbers)
