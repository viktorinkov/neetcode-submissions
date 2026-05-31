# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## high level
        
        ## go through all the first nodes of all the lists
        ## find the node with the lowest value
        ## this is the start node
        res = ListNode(0)
        curr = res

        while True:

            ## go through all nodes and find smallest of next ones
            minNode = -1
            minVal = float('inf')
            for i in range(len(lists)):
                if(lists[i] is not None and lists[i].val < minVal):
                    minNode = i
                    minVal = lists[i].val

            if(minNode == -1):
                break

            curr.next = lists[minNode]
            curr = curr.next
            lists[minNode] = lists[minNode].next


        return res.next
                
        
        