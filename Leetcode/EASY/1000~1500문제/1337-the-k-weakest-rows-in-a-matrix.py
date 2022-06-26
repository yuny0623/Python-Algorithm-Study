'''
~ 400

Runtime: 137 ms, faster than 68.20% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.5 MB, less than 13.92% of Python3 online submissions for The K Weakest Rows in a Matrix.

코멘트: 
꽤나 재밌는 문제다. 그런데 로직 중 한군데를 살짝 이상하게 짜서 10분 정도를 낭비했다. 
지금 아래 코드가 꽤나 긴데 문제 자체가 쉬운것에 비하면 지나치게 길다. 이거 충분히
짧게 만들 수 있을 것 같다. -> 개선해봅시당. 
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = [0] * len(mat)
        for i in range(len(mat)):
            li[i] = mat[i].count(1)
        
        print(f'li:{li}')
        sorted_li = sorted(li)
        print(f'sorted_li:{sorted_li}')
        result = [0] * k
        j = 0
        for i in range(len(sorted_li)):
            print(f'li in loop :{li}')
            result[j] = li.index(sorted_li[i])
            idx = li.index(sorted_li[i])
            li[idx] = -1
            j += 1
            if j == k:
                break
        print(li)
        print(result)
        return result 

'''
Runtime: 214 ms, faster than 16.04% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.2 MB, less than 87.40% of Python3 online submissions for The K Weakest Rows in a Matrix.

개선한 솔루션: 
역시 list comprehension 이 상당히 좋다. 그냥 가독성이 너무 좋다. 
근데 여기서도 더 줄일 수 있을까? 그리고 항상 leetcode 풀면서 느끼는 거지만 실행속도와 메모리가
매번 돌릴때마다 다르게 나온다. 근사치가 아니라 완전 상이한 값이 나온다. 즉 릿코에서 
이걸로 잘짰는지 못짰는지 평가할게 못된다. 그냥 코드나 이쁘게 짜는게 나을듯. 
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = [row.count(1) for row in mat] # list comprehension 으로 수정해서 코드 줄였음. 
        sorted_li = sorted(li) 
        
        result = [0] * k
        j = 0
        for i in range(len(sorted_li)):
            idx = li.index(sorted_li[i])
            result[j] = idx
            li[idx] = -1
            j += 1
            if j == k:
                break
                
        return result 


'''
개선했지만 오답인 솔루션: 
여기까지는 어떻게 list comprehension 으로 바꿔줬는데 list comprehension에서 선언문을 
실행안될것같은데...즉 위 코드에서 보면 -1 로 설정하는 부분이 있는데 즉 할당이 list comprehension
에서 이뤄질 수 있는지 모르겠다. 이건 찾아보자. 

:= 엱산자를 통해서 할당할 수 있는 기능이 있다는 답변이 Stackoverflow 에 있었는데 나와 같은
경우에 사용할 수 있는 연산자가 아니다. 즉 list comprehension 내에서 한번에 끝낼 수 있는 
방법이 아니다. 
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = [row.count(1) for row in mat] 
        sorted_li = sorted(li) 
        result = [li.index(val) for val, count in zip(sorted_li, list(range(k))) if count <k]
        return result 
    