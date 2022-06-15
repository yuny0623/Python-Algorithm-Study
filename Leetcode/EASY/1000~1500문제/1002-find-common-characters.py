'''
0455 ~ 답지보고 풀음 

코멘트: 
풀이가 직관적으로 떠오르진 않는다. 
문제 난이도 자체는 쉬움. 다만 풀이 방법이 상당히 다양할듯 싶음. 

어떻게 풀지... 
모든 word 에 대해서 전부다 투포인터로 돌아야되..? 흑흑 

쉬운것같은데 왜 안풀리지. 
'''

'''
오답 솔루션: 
이건 접근 방법이 틀린것 같다. 
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        sorted_words = []
        for word in words:
            sorted_words.append(sorted(word))
        sorted_words = sorted(sorted_words, key = lambda x: len(x))
        if len(words) == 1:
            return words[0]
        
        common_char = []
        first_word = sorted_words[0]
        for c in first_word:
            flag = True
            for i in range(1, len(words)):
                if c not in words[i]:
                    flag = False
            if flag:
                common_char.append(c)
                
        return common_char
            
            
'''
정답 솔루션: 
Runtime: 71 ms, faster than 54.42% of Python3 online submissions for Find Common Characters.
Memory Usage: 13.9 MB, less than 95.44% of Python3 online submissions for Find Common Characters.

코멘트: 
답지보고 풀었다. 
참고로 'a' 같은 단일 char에 대해서 int() 쓰면 에러 난다. 
이때는 ord() 를 사용해라. 아래 아이디어를 떠올리지 못해서 못풀었다. 
'''          

import sys
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alpha = [sys.maxsize] * 26
        
        for word in words:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            
            for i in range(26):
                alpha[i] = min(alpha[i], temp[i])
            
        result = [] 
        for i in range(26):
            if alpha[i] != 0:
                while alpha[i] != 0:
                    result.append(chr(i+ord('a')))
                    alpha[i] -= 1
        
        print(result)
        return result 
            
                    
        
        

