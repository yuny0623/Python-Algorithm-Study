class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 아마 스택 써야겠지? 
        front_stack = []
        back_stack = [] 
        front = ['(', '[', '{']
        back = [')',']' , '}']
        
        if len(s)%2 == 1:
            return False 
        
        for i in range(len(s)):
            if s[i] in front:
                front_stack.append(s[i])
            if s[i] in back: 
                back_stack.append(s[i])
                if len(front_stack) == 0:
                    return False
                else: 
                    f = front_stack.pop()
                    if front.index(f) != back.index(s[i]):
                        front_stack.append(f)
                        return False
        if len(front_stack) == 0:
            return True
        else:
            return False
        