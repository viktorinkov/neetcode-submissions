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
        # two pass
        if(head == None):
            return None
        mydict = {}
        cur = head
        # pass 1 for mydict[oglist] = newnode
        while cur:
            tmp = Node(cur.val, None, None)
            mydict[cur] = tmp
            cur = cur.next
        
        # pass 2
        cur = head
        while cur:
            mydict[cur].next = mydict.get(cur.next, None)
            mydict[cur].random = mydict.get(cur.random, None)
            cur = cur.next

        return mydict[head]