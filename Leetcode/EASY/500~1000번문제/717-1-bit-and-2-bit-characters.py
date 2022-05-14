'''
0359 ~ <답지보고 풀음>

살짝 안풀리네 어떻게 풀까요 
0420 
그냥 구현이 아니라 다른 접근법이 있는 문제인듯. 

0427
지문를 이해를 못함 ㄷㄷ 

Runtime: 93 ms, faster than 18.79% of Python3 online submissions for 1-bit and 2-bit Characters.
Memory Usage: 17 MB, less than 5.03% of Python3 online submissions for 1-bit and 2-bit Characters.

코멘트: 

'''
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits == [0]:
            return True
        if bits == [1, 0] or bits == [1, 1]:
            return False
        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        if bits[0] == 1:
            return self.isOneBitCharacter(bits[2:])
        
        
        
        
 