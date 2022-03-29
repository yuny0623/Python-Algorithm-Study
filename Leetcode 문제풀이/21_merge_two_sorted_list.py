# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    
        if list1 == None and list2 is not None:
            return list2
        if list2 == None and list1 is not None:
            return list1 
        if list1 == None and list2 == None:
            return None
        if list1.val < list2.val:
            result = ListNode(list1.val, None)
            list1 = list1.next 
            max_val = 0 
            head = result 
        else: 
            result = ListNode(list2.val, None)
            list2 = list2.next  
            max_val = 0 
            head = result 

        while list1 != None:
            if list1 == None or list2 == None:
                break 
            if list1.val > list2.val:
                result.next = ListNode(list2.val, None)
                result = result.next
                list2 = list2.next
                continue
            if list1.val == list2.val:
                result.next = ListNode(list1.val, None)
                result = result.next
                result.next = ListNode(list2.val, None)
                result = result.next
                list1 = list1.next
                list2 = list2.next
                continue
            if list2.val > list1.val:
                result.next = ListNode(list1.val, None)
                result = result.next
                list1 = list1.next
                continue
                
        if list1 != None:
            while list1 != None:
                result.next = ListNode(list1.val, None)
                result = result.next
                list1 = list1.next
        if list2 != None:
            while list2 != None: 
                result.next = ListNode(list2.val, None)
                result = result.next
                list2 = list2.next
            
        return head 
        
        