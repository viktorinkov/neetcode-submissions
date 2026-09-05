"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # two iterations
        # fix next
        # fix random
        # O(n)
        prev = Node(-101)
        copyRef = prev
        rootRef = head
        refMap = {} # ogList : newList

        while head:
            curr = Node(head.val) # 3
            refMap[head] = curr
            prev.next = curr # 
            prev = curr # 
            head = head.next # head = None

        # prev = Node(3)
        # head = None

        head = rootRef
        
        while head:
            curr = refMap[head]
            curr.random = refMap.get(head.random, None)
            head = head.next

        return copyRef.next

            

        
        


        