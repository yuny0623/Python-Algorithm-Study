'''
0926 ~ 0934 

Runtime: 60 ms, faster than 24.59% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.8 MB, less than 98.66% of Python3 online submissions for Unique Morse Code Words.

코멘트: 
사실 이 문제는 문제 자체를 이해 못했다.
그냥 예시보고 풀었다. 근데 어렵진 않다. 그저 set 개수 구해주는게 다이다. 
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        char = 'abcdefghijklmnopqrstuvwxyz'
        
        d = dict()
        for a, b in zip(char, morse):
            d[a] = b
        
        result = []
        for w in words:
            morse_str = []
            for c in w:
                morse_str.append(d[c])
            result.append(''.join(morse_str))
        return len(set(result))
            
        
        
        
        