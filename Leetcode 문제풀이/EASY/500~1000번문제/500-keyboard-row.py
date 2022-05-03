'''
0822 ~ 1037 
예외만 잘생각하고 풀면됨.
생각보다 코드가 너무 길어졌네 
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        result = [] 
        for i in range(len(words)):
            past = None 
            now = None 
            if words[i][0].lower() in row1:
                past = 'row1'
                now = 'row1'
            elif words[i][0].lower() in row2:
                past = 'row2'
                now = 'row2'
            elif words[i][0].lower() in row3:
                past = 'row3'
                now = 'row3'
                
            for j in range(len(words[i])): 
                if now != past:
                    break 
                if words[i][j].lower() in row1:
                    now = 'row1'
                elif words[i][j].lower() in row2:
                    now = 'row2'
                elif words[i][j].lower() in row3:
                    now = 'row3'
            print(now, past)
            if now == past:
                result.append(words[i])
                    
        return result 
                
                
                