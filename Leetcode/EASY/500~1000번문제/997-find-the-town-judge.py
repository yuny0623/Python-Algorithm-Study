'''
0115 ~ 0140 
Runtime: 2240 ms, faster than 5.02% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19 MB, less than 66.41% of Python3 online submissions for Find the Town Judge.

코멘트: 
꽤나 흥미로운 문제다. 구현 자체는 어렵지 않음. 하지만 지문에 명시되지 않은 예외케이스가 하나 
숨어있음. 그걸 잘 찾아서 가드로 잘 막아주면 쉽게 풀 수 있을 거임. 

'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        if len(trust) == 0 and n != 1:
            return -1
        
        person = list(set([x for li in trust for x in li]))
        person_original = person[:]
        for i in range(len(trust)):
            if trust[i][0] in person: 
                person.remove(trust[i][0])
        
        if len(person) == 0:
            return -1
        town_judge = person[0]
        
        for i in range(1, n + 1):
            if i == town_judge:
                continue 
            print([i, town_judge])
            if [i, town_judge] not in trust:
                return -1 
        
        return town_judge
        