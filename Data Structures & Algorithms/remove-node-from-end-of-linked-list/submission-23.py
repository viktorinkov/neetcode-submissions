# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_depth(head, depth):
            if(head is None):
                return depth
            else:
                return get_depth(head.next, depth+1)
        
        final_depth = get_depth(head, 0)
        print(final_depth)

        if final_depth == n:
            return head.next

        def dfs(head, idx):
            print(f"difference {final_depth - idx}")
            if(head is None):
                return
            else:
                if(final_depth - idx == n):
                    print(f"element to be removed {head.val}")
                    return - 1
                else:
                    if(dfs(head.next, idx + 1) == -1):
                        if(head.next and head.next.next):
                            head.next = head.next.next
                        else:
                            head.next = None    
                        return
        if(final_depth < 2):
            return None
        dfs(head, 0)
        return head
                    




        

        