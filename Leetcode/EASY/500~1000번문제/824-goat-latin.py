'''
1033 ~ 1039 
Runtime: 42 ms, faster than 48.20% of Python3 online submissions for Goat Latin.
Memory Usage: 13.7 MB, less than 97.86% of Python3 online submissions for Goat Latin.

코멘트: 
이거 대문자일 경우도 잡아줘야함. 그래서 AEIOU 도 검사해줘야함. 
쉬운문제
'''

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = [] 
        i = 1
        for w in sentence.split():
            if w[0] in 'aeiouAEIOU':
                result.append(w + 'ma' + ('a'* i))
            elif w[0] not in 'aeiouAEIOU':
                result.append(w[1:] + w[0] + 'ma'+ ('a'* i))
            i += 1

        return ' '.join(result)