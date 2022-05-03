'''
0916 ~ 0927 

Runtime: 59 ms, faster than 12.43% of Python3 online submissions for Detect Capital.
Memory Usage: 13.8 MB, less than 55.38% of Python3 online submissions for Detect Capital.

이 문제는 문제 해석 자체가 좀 헷갈릴 여지가 있었음. 
그래도 꽤 쉬운편. 

코드가 꽤 지저분하지? 개선 가능? 
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 2:
            if len(word) == 2:
                if word[0].islower() and word[1].isupper():
                    return False 
            return True 
        if word[0].islower():
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
            return True 
        else:
            if word[1].islower():
                for i in range(2, len(word)):
                    if word[i].isupper():
                        return False
                return True 
            else:
                for i in range(1, len(word)):
                    if word[i].islower():
                        return False
                return True 
'''
개선 코드2:
Runtime: 42 ms, faster than 48.92% of Python3 online submissions for Detect Capital.
Memory Usage: 13.9 MB, less than 10.84% of Python3 online submissions for Detect Capital.

좀더 개선 가능? 
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True 
        if word[0].islower():
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
            return True 
        else:
            if word[1].islower():
                for i in range(2, len(word)):
                    if word[i].isupper():
                        return False
                return True 
            else:
                for i in range(1, len(word)):
                    if word[i].islower():
                        return False
                return True 


'''
개선한 코드3: 

Runtime: 30 ms, faster than 88.13% of Python3 online submissions for Detect Capital.
Memory Usage: 13.9 MB, less than 55.38% of Python3 online submissions for Detect Capital.

확실히 빨라졌다. 뭐든 length 는 미리 구해놓고 쓰자. 괜히 그때마다 계산하면 필요없는 오버헤드생김. 
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = len(word)
        if l < 2:
            return True 
        if word[0].islower():
            for i in range(1, l):  
                if word[i].isupper():
                    return False
        else:
            if word[1].islower():
                for i in range(2, l):
                    if word[i].isupper():
                        return False
            else:
                for i in range(1, l):
                    if word[i].islower():
                        return False
        
        return True 
            

            