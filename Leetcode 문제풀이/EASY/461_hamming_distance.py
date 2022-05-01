'''
0249 ~ 0312 
쉬움. 근데 bin() 하고 나서 처리가 좀 귀찮아용 -> 아니네요
이거 문자열로 풀려고 했다가 20분날림. 비트마스크로 1분만에 풀음. 
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
            
                
        
        
        
        
        
