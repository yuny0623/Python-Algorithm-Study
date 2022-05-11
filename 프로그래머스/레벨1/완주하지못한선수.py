'''
0929 ~ 0937 

첫번째 제출한 코드가 효율성에서 탈락했다. 그래서 아래처럼 조금 불필요한 코드를
많이 쓰게 되었다. 여기서 defaultdict 를 통해서 조금 더효율적인 코드를 만들 수 있을까? 

팁:
collections.Counter 쓰신 분이 계신다.
참고로 Counter 객체는 뺄셈이 가능하다. 
'''
def solution(participant, completion):
    d = dict() 
    for p in participant:
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1
        
    for c in completion:
        d[c] -= 1
    
    for key, value in d.items():
        if value == 1:
            return key 
            
'''
아래처럼 Counter 를 활용해도 좋을듯싶다.
'''
import collections 
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]