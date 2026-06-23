# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #inithoughts: start linking from the back
        #[0, 1, 2, 3, n-2, n-1] -> [0, n-1, 1, n-2, 2, 3]
        #doesnt work, lets try 1. finding middle 2. cut into half and reverse second 3. merge alternately

        #1.finding middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #now slow will be pointing towards the middle (floored if even)

        #2.cut and reverse
        part2 = slow.next
        slow.next = None
        prev = None
        curr = part2
        while curr != None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp 
        #now prev is the head of the reversed second part
        # print(head.val, head.next.val)
        # print(prev.val, prev.next.val)

        #3.merge alternately
        part1 = head
        part2 = prev
        while part1.next:
            part1_next_temp = part1.next
            part1.next = part2
            part2 = part2.next 
            part1.next.next = part1_next_temp
            part1 = part1.next.next
        if part2:
            part1.next = part2