'''
1235 ~ 1242 

코멘트: 
문제 그대로 구현하면 되는 문제 
근데 이거 정규표현식으로 풀 수 있을 것 같은데 ... 
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 룰1: local name 에 dot 을 붙이면 dot없는거랑 똑같은 곳으로 전송됨 
        # 룰2: local name 에 + 를 붙이면 + 뒤는 전부 무시됨. 
        new_emails = [] 
        for email in emails:
            local = email[0:email.find('@')]
            new_local = []
            for c in local:
                if c == '.':
                    continue 
                elif c == '+':
                    break
                else:
                    new_local.append(c)
            new_local = ''.join(new_local)
            new_emails.append(new_local + email[email.find('@'):])
        print(new_emails)
        
        return len(list(set(new_emails)))
