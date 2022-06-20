'''
1031 ~ 1041 

Runtime: 329 ms, faster than 28.43% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.4 MB, less than 84.98% of Python3 online submissions for Find Words That Can Be Formed by Characters.s

코멘트: 
흠 왜 난 항상 같은 솔루션을 만들어도 코드가 길게 나오는걸까... <- 코드 줄이기도 연습해봅시다. 
'''
from collections import defaultdict 
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        d = defaultdict(int)
        for c in chars:
            d[c] += 1
            
        sum_of_lengths = 0 
        for word in words:
            d_word = defaultdict(int)
            for c in word:
                d_word[c] += 1
            
            is_in = True
            for k, v in d_word.items():
                if k not in d:
                    is_in = False 
                    break 
                if v > d[k]:
                    is_in = False 
                    break 
                    
            if not is_in:
                continue 
            
            sum_of_lengths += len(word)
            
        return sum_of_lengths 

'''
코드 줄인 솔루션: 

Runtime: 126 ms, faster than 88.82% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.6 MB, less than 36.59% of Python3 online submissions for Find Words That Can Be Formed by Characters
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum_of_lengths = 0 
        for word in words:
            flag = True  
            for c in word:
                if word.count(c) > chars.count(c):
                    flag = False 
                    break
            if flag: 
                sum_of_lengths += len(word)
        return sum_of_lengths 
        
                
                     
