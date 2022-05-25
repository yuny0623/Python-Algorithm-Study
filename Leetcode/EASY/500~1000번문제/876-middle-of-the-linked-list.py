'''
0541 ~ <밥먹고옴ㅋ> ~ 0616 

Runtime: 66 ms, faster than 5.64% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14 MB, less than 10.83% of Python3 online submissions for Middle of the Linked List.

코멘트:
딱 보고 런너 생각안나면 시간 낭비할 문제임. 
런너 떠오르면 바로 풀림. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 아 이거 런너같은데... 
        # 런너로 풀어야할 것 같은 느낌이 든다... 
        middle = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow 
            

