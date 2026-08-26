class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        res = ListNode()
        copy = res

        while l1 and l2:
            temp = l1.val + l2.val
            temp += carry

            if temp > 9:
                carry = 1
            else:
                carry = 0

            res.val = temp % 10

            if l1.next or l2.next or carry:
                newNode = ListNode(carry)
                res.next = newNode
                res = newNode

            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = l1.val
            temp += carry

            if temp > 9:
                carry = 1
            else:
                carry = 0

            res.val = temp % 10

            if l1.next or carry:
                newNode = ListNode(carry)
                res.next = newNode
                res = newNode

            l1 = l1.next

        while l2:
            temp = l2.val
            temp += carry

            if temp > 9:
                carry = 1
            else:
                carry = 0

            res.val = temp % 10

            if l2.next or carry:
                newNode = ListNode(carry)
                res.next = newNode
                res = newNode

            l2 = l2.next

        return copy