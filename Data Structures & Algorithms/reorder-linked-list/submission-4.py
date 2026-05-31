# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        ## reverse l2
        curr, prev = l2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ## prev is now first element
        l1 = head
        l2 = prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
            