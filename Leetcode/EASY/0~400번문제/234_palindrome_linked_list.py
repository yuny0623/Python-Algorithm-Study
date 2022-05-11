from typing import Optional, ListNode 
'''
0916 ~ 0927 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        rev = None 
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next 
            
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != rev.val:
                return False 
            slow = slow.next
            rev = rev.next 
            
        return True 
            