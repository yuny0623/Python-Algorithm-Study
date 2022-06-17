'''
1146 ~ <못품> ~ <0616 다시풀기> ~ <0617 다시풀기> ~ 

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
        
            
'''
정답 솔루션:
Runtime: 47 ms, faster than 48.31% of Python3 online submissions for Long Pressed Name.
Memory Usage: 14.1 MB, less than 10.12% of Python3 online submissions for Long Pressed Name.

일단 어떻게 풀어야할지 감은 잡았다. 이 문제는 작은 두 개의 문제로 다시 나눌 수 있다. 
하나는 단어에 포함되는 알파벳의 개수를 따지는 문제고 
하나는 실제 단어의 ordering이 즉 순서가 같아야 원래 타이핑하려던 이름이 실제 이름과 같은지를 따지는 문제다. 

예외 케이스 잡느라 불필요한 조건문이 많아졌는데 이것도 로직이 정확하지 못해서 그렇다. 
개선가능할듯 
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
        
        print("checking same ordering...")
        
        i = 0 # name 
        j = 0 # typed 
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            else:
                if j != 0  and typed[j - 1] != typed[j]:
                    return False 
            if j == 0 and i == 0 and typed[j] != name[i]:
                return False 
            j += 1
        if name[-1] != typed[-1]:
            return False 
        return True 
                
            











