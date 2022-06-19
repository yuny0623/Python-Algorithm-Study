'''
0919 ~ <답지보고풀음>

코멘트: 
로직이 명확하게 생각이 안남. 스택을 활용해야함. 
'''
'''
오답 솔루션: 
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        li = list(s)
        while True:
            print(li)
            count = 1
            for i in range(1, len(li)):
                if li[i - 1] == li[i]:
                    count += 1
            if count == 1:
                return ''.join(li) 
            
            new_li = [] 
            i = 1
            while i < len(li):
                if li[i - 1] == li[i]:
                    i += 1
                else:
                    new_li.append(li[i - 1])
                i += 1
            li = new_li 
                    
        return ''.join(li)

'''
정답 솔루션: 
Runtime: 131 ms, faster than 41.59% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 14.8 MB, less than 48.07% of Python3 online submissions for Remove All Adjacent Duplicates In String.

코멘트:
스택을 활용하자. 
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            char = s[i]
            if len(stack) == 0:
                stack.append(char)
            elif len(stack) >= 1:
                if stack[-1] == char:
                    stack.pop()
                    continue
                else:
                    stack.append(char)
                    
        return ''.join(stack)




