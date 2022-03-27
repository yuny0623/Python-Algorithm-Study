
# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#     if (not l1) or (l2 and l1.val > l2.val):
#         l1, l2 = l2, l1
#     if l1:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#     return l1 

def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        # 아마 스택 써야겠지? 
        stack = []
        front = ['(', '[', '{']
        back = [')',']' , '}']
        for i in range(len(s)):
            if s[i] in front:
                stack.append(s[i])
                continue 
            if s[i] in back: 
                symbol = stack.pop()
                if symbol != s[i]:
                    return False

        return True

print(isValid("()"))