'''
0442 ~ 0508 
쉬운데 예외케이스가 있는 문제임. 
전부다 dash 로 있을때는 어떻게 할건지? <- 예외 고려해서 코드 추가해줘야됨.

아마 코드 개선할 수 있을듯 
'''

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        
        new_s = [] 
        for c in s:
            if c != '-':
                new_s.append(c)
        
        result = []
        count = 0 
        for i in range(len(new_s)):
            result.append(new_s[i].upper())
            count += 1
            if count % k == 0:
                result.append('-')
        
        if len(result) != 0 and result[-1] == '-':
            result.pop() 
        
        return ''.join(result)[::-1]

        
        
        