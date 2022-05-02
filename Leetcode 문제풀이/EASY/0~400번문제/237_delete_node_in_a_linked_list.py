'''
1053 ~ 1106 

결국은 마지막 원소를 삭제하는게 포인트임. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        cur.val = cur.next.val
        cur.next = cur.next.next 
        
        while cur.next:
            cur = cur.next
        cur = None 
            
        return cur 
        
