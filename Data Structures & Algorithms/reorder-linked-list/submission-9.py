# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head.next is None):
            return
            
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at midpoint
        midpoint = slow

        # form l2 in reverse
        l2 = midpoint.next
        midpoint.next = None

        prev = None
        while l2 is not None:
            # 1, 3, 5
            # 1 -> None, l2 = 3
            # 3 -> 1 -> None, l2 = 5
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp

        reversed_l2 = prev # opposite list
        l1 = head

        while reversed_l2:
            temp = l1.next
            temp2 = reversed_l2.next

            l1.next = reversed_l2
            reversed_l2.next = temp

            l1 = temp
            reversed_l2 = temp2