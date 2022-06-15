'''
0717 ~ 



코멘트: 
아 이거 생각보다 안풀린다. 30분째 고전중... 
예외케이스가 숨어있는데 그게 좀 많이 까다롭다. 문제에 나와있는게 아닌데 
submit했을때 발견할 수 있는 예외... 
'''

'''
오답 솔루션: 
여기서도 예외를 잡지 못했다. 여기서 살짝 수정만 해주면 솔루션얻을 수 있을 것 같다. 
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log = []
        letter_log = [] 
        
        for l in logs:
            li = l.split()
            if li[1].isdigit():
                digit_log.append(l)
            else:
                letter_log.append(l)
        
        print(digit_log)
        print(letter_log)
        
        letter_log = sorted(letter_log, key = lambda x: x.split()[1:]) # 여기서 정렬 진행 
        
        # 수정해주는 코드를 추가하자. 
        print(letter_log)
        
        new_letter_log = [] 
        for i in range(1, len(letter_log)):
            if letter_log[i-1].split()[1:] == letter_log[i].split()[1:]: # 만약 요소가 같다면? 
                new_letter_log.append(letter_log[i - 1])
        if len(new_letter_log) == 0:
            return letter_log + digit_log
        new_letter_log.append(letter_log[-1])
        new_letter_log = sorted(new_letter_log)
        
        return new_letter_log + digit_log
        
        