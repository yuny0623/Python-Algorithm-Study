'''
0924 ~ 0926 

내적문제. zip 을 활용했다. 
'''
def solution(a, b):
    total = 0
    for c, d in zip(a, b):
        total += c*d
    return total


'''
다른 사람 풀이 문제란을 보던 중 조금 더 간결한 코드를 발견했다. 

항상 간결한 코드는 언어의 특성을 적극 활용한 코드인듯
특히 파이썬에서 list comprehension을 쓴 코드를 많이보는것같다. 
'''
def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])