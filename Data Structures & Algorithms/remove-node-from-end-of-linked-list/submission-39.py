# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse once to get n count
        # traverse second time to remove correct node
        counter = head
        count = 0
        while counter:
            count += 1
            counter = counter.next
        if(count == 1):
            return None
        if(count == n):
            return head.next
        k = count - n # 4 - 2 = 2

        i = 0
        counter = head
        while i <= k:
            if(i == k - 1): # delete next node
                if(counter.next and counter.next.next):
                    counter.next = counter.next.next
                else:
                    counter.next = None
            i += 1
            if(counter):
                counter = counter.next
            else:
                break
        return head