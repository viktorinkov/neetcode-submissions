# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        tmp = None

        while curr:
            tmpnext = curr.next
            curr.next = tmp
            tmp = curr
            curr = tmpnext

        return tmp
        
        # 0, 1, 2, 3
        # tmpnext = 1
        # 0.next = None
        # tmp = 0
        # curr = 1
        # 2nd it
        # tmpnext = Node(1, next None)
        # curr.next = 0 (correct)
        # tmp = Node(1, next 0)
        # curr = Node(1, next None)
