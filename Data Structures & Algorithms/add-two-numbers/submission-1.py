# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we build the answer node by node
        # have a dummy node and return answer dummy.next 
        # always append to tail.next
        dummy = ListNode(0)
        tail = dummy

        # carry holds the overflow from the prev column summation
        # always 0 or 1
        carry = 0

        # walk both lists together from the head, 
        # which is the same order as we want to do the summation 
        current1, current2 = l1, l2 

        while current1 is not None or current2 is not None:
            if current1 is not None:
                digit1 = current1.val
            else:
                digit1 = 0
            
            if current2 is not None:
                digit2 = current2.val
            else:
                digit2 = 0

            column_sum = digit1 + digit2 + carry
            digit_to_store = column_sum % 10
            carry = column_sum // 10
            tail.next = ListNode(digit_to_store)
            tail = tail.next

            # advance points that still have nodes left
            if current1 is not None:
                current1 = current1.next
            if current2 is not None:
                current2 = current2.next
        
        # handle a leftover carry
        if carry > 0:
            tail.next = ListNode(carry)
            tail = tail.next

        return dummy.next
        