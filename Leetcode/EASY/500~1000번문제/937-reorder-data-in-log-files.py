'''
0717 ~ <못풀었음> ~ <0616 한숨자고 다시풀게용.> ~ <모르겠음>

코멘트: 
아 이거 생각보다 안풀린다. 30분째 고전중... 
예외케이스가 숨어있는데 그게 좀 많이 까다롭다. 문제에 나와있는게 아닌데 
submit했을때 발견할 수 있는 예외... 
'''

'''
오답 솔루션1: 
여기서도 예외를 잡지 못했다. 여기서 살짝 수정만 해주면 솔루션얻을 수 있을 것 같다. 
일단 대충 감은 잡음. 이건 답지 안보고 풀어보자. 
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
        
        

'''
오답 솔루션2:
이것도 틀렸다. 너무 코드가 길어짐. 분명 이렇게 푸는게 아닌것 같다.  
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
        
        # 룰
        # 1. letter_log는 digit_log 보다 선행된다. 
        # 2. letter_log는 사전순 정렬된다. 내용이 같은게 있다면 구분자에 의해 사전순 정렬한다. 
        # 3. digit_log는 주어진 순서를 유지한다. 
        
        sorted_letter_log = sorted(letter_log, key = lambda x: x.split()[1:]) # 1차 정렬 
        
        if len(sorted_letter_log) == 1: # 길이가 1이라면 바로 리턴 
            return sorted_letter_log + digit_log
        
        fixed_letter_log = [] 
        temp = [] 
        print(sorted_letter_log)
    
        start = 0
        end = 0
        while end < len(sorted_letter_log):
            if sorted_letter_log[start][1:] == sorted_letter_log[end][1:]:
                end += 1
                continue
            else:
                if end - start > 1: 
                    fixed_letter_log += sorted(sorted_letter_log[start:end], key = lambda x: x.split()[0])
                else:
                    fixed_letter_log.append(sorted_letter_log[end])
                start = end 
                end += 1
        fixed_letter_log.append(sorted_letter_log[end - 1])
        print("fixed_letter_log:{0}".format(fixed_letter_log))
        return fixed_letter_log + digit_log 


