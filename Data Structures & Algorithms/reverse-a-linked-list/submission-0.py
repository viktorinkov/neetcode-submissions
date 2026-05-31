# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ## 0, next = 1
        ## 1, next = None
        ## head is 0
        ## temp = 1
        ## 0.next = None

        ## prev = 0, None
        ## curr = 1, None

        ## second iteration
        ## temp = None
        ## 1.next = 0
        ## prev = Node(1, 0)
        ## 


        
        return prev