# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        result = ListNode()
        dummy = result

        while curr1 and curr2:
            if(curr1.val < curr2.val):
                result.next = curr1
                curr1 = curr1.next
            else:
                result.next = curr2
                curr2 = curr2.next
            
            result = result.next
        
        while curr1:
            result.next = curr1
            curr1 = curr1.next
            result = result.next

        while curr2:
            result.next = curr2
            curr2 = curr2.next
            result = result.next 

        ## list1 = [1,2,4], list2 = [1,3,5]

        ## result = 0, None
        ## curr1 = 1
        ## curr2 = 1
        ## loop 1
        ## result = 0, 1
        ## curr2 = 3
        ## loop 2
        ## result = 

        return dummy.next