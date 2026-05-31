# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        ahead = head
        for i in range(n):
            ahead = ahead.next
        
        if ahead is None:
            return first.next

        while ahead:
            if(ahead.next is None):
                if(first.next):
                    first.next = first.next.next
                else:
                    first.next = None
                break
            else:
                first = first.next
                ahead = ahead.next

        return head