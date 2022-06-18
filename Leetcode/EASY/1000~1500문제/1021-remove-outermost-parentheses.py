'''
0801 ~ <답지보고 풀음> ~ 0930 

Runtime: 46 ms, faster than 75.35% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 14 MB, less than 60.84% of Python3 online submissions for Remove Outermost Parentheses.

코멘트: 새로운 유형. 
'''
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # 새로운 유형이다. 처음 보는 문제임. 
        check = 0
        stack = [] 
        for c in s:
            if c == '(':
                check += 1
                if check > 1:
                    stack.append(c)
                
            if c == ')':
                check -= 1
                if check >= 1:
                    stack.append(c)
        
        return ''.join(stack)