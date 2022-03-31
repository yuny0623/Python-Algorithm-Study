from typing import Optional, ListNode 
'''
0445 ~ 0515 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = []
        start = head 
        while head != None:
            if head.val == val:
                head = head.next
                continue 
            result.append(head.val)
            head = head.next
            
        if len(result) == 0: 
            return None 
        
        new_start = ListNode(result[0])
        r = new_start
        for i in range(1, len(result)):
            new_start.next = ListNode(result[i])
            new_start = new_start.next 
            
        return r
            
            
