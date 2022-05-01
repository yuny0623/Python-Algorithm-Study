'''
0951 ~ 0244 

꽤 재밌는 문제임. 그렇게 안어려움. 그냥 반복만 제대로 돌면됨. 
for 에 있는 range 에서 +1 없애면 오답임. 왤까용. // 을 쓰면 정수로 내림처리됨. 
-> +1 해서 올림으로 잡읍시다.  
'''
class Solution: # abab 
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1): # 4//2 -> 2 
            sub_string = s[0:i] # ab 
            times = len(s) // i # 4 // 2 -> 2 
            new_s = sub_string * times  # -> ab * 2 -> abab 
            if new_s == s:
                return True
            else:
                continue
            
        return False 