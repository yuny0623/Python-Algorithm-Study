from typing import Optional, ListNode
'''
0900 ~ 0907 
런너기법에서 코드 훔치기 ㄷㄷ 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None 
        start = head
        while start != None:
            rev, rev.next, start = start, rev, start.next
        return rev 