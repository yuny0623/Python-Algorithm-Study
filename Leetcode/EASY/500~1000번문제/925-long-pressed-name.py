'''
1146 ~ <못품> ~ <0616 다시풀기> ~ 

코멘트: 
왜 이거 다들 쉽다는데 나만 어려운것같지? 
'''
'''
오답 솔루션: 
'''
from collections import defaultdict 
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == len(typed):
            if name == typed: # 같은 이름일 경우 
                return True
        if len(name) > len(typed):
            return False 
            
        i = 0
        j = 0
    
        while i < len(name):
            if i < len(name) and name[i] == name[j]:
                i += 1
            else: 
                if j == 0 or name[i] != name[j]:
                    return False 
            j += 1
            
        return i == len(name)
        
    
        
'''
오답솔루션2: 
예외케이스 딱 하나에서 걸리는데 지문에서는 나오지 않은 동작으로 걸린다. 뭘까. 
''' 
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        min_alpha = [0] * 26 
        typed_alpha = [0] * 26
        for n in name:
            min_alpha[ord(n) - ord('a')] += 1
        
        for t in typed:
            typed_alpha[ord(t) - ord('a')] += 1
    
        for c1, c2 in zip(min_alpha, typed_alpha):
            if c1 > c2:
                return False 
            
        word1 = [typed[0]]
        for i in range(1, len(typed)):
            if typed[i] == word1[-1]:
                continue
            else:
                word1.append(typed[i])
                
        word2 = [name[0]]
        for i in range(1, len(name)):
            if name[i] == word2[-1]:
                continue
            else:
                word2.append(name[i])
                
        print(word1, word2)
        if word1 == word2:
            return True
        else:
            return False 
        
            










