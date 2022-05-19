'''
1144 ~ 0155 
Runtime: 155 ms, faster than 17.46% of Python3 online submissions for Shortest Completing Word.
Memory Usage: 14.3 MB, less than 17.64% of Python3 online submissions for Shortest Completing Word.

코멘트:
생각보다 로직이 직관적으로 떠오르지 않는 문제.
예외가 몇가지 있음. 그리고 깊은 복사를 하지 않아서 많이 헤맸는데 결국 
깊은 복사를 함으로써 해결했음. 근데 별로 좋은 방법으로 보이진 않음. 
깊은 복사 쓰지 않고 하는 방법은 없을까? 
'''
from collections import defaultdict
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        remove_digit = []
        for c in licensePlate:
            if c.isalpha():
                remove_digit.append(c.lower())
        licensePlate = ''.join(remove_digit)   
        words = [x.lower() for x in words]
    
        d = defaultdict(int)
        for c in licensePlate:
            d[c] += 1
        completing_word = []
        for w in words:
            co = d.copy()
            print(co)
            if (set(w) & set(licensePlate)) != set(licensePlate) :
                continue
            for c in w:
                if c in co and co[c] != 0:
                    co[c] -= 1
            print("w:{0},co:{1}".format(w,co))
            if sum(co.values()) == 0:
                completing_word.append((len(w), w))
        
        completing_word = sorted(completing_word, key = lambda x: x[0])
        return completing_word[0][1]
        


'''
개선한 솔루션: 
'''



