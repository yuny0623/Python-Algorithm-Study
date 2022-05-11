'''
정규 표현식 라이브러리 사용하는 방법을 알면 정말 쉽게 풀 수 있는 문제임
한시간 걸렸다...

참고: 정규식 안쓰면 어떻게 풀 수 있을까...? 
-> while 문활용하신 분이 게셨다. 
while '..' in new_id:
    new_id.replace('..', '.')
이렇게 쓰신 분이 계셨다. 즉 문자열 내에서 '..' 없앨때까지 계속 돌겠다는 뜻이다. 
기발하시네. 
'''

import re
def solution(new_id):
    new_id = new_id.lower() # 1단계 
    new_str2 = [] 
    for c in new_id: # 2단계 
        if (c.isalpha() or c.isdigit() or (c in '-_.')):
            new_str2.append(c)
            
    new_str3 = ''.join(new_str2) # 3단계  
    new_str3 = re.sub('.{2}','.', new_str3)
            
    
    if len(new_str3) == 1 and new_str3 == '.':
        new_str3 = ''
    else:
        if new_str3[0] == '.': # 4단계 
             new_str3 = new_str3[1:]
        if new_str3[len(new_str3) - 1] == '.':
            new_str3 = new_str3[:-1]
    
    if len(new_str3) == 0: # 5단계 
        new_str3 = 'a'
    
    if len(new_str3) >= 16:
        new_str3 = new_str3[:15]
    if new_str3[-1] == '.':
        new_str3 = new_str3[:-1]
    
    if len(new_str3) <= 2:
        last = new_str3[-1]
        while len(new_str3) < 3:
            new_str3 += last 
            
    return new_str3 

print(solution('...!@BaT#*..y.abcdefghijklm'))