# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None

        def helper(node):
            print("checking", node.val)
            temp = node
            is_correct_node = False
            for _ in range(0,n):
                if temp.next:
                    temp = temp.next
                else:
                    print("found node to be removed:", node.val)
                    is_correct_node = True
            return is_correct_node


        # means i remove head
        if helper(head):
            head = head.next
        else:
            curr = head
            while curr:
                # means i remove the next node
                if helper(curr.next):
                    temp = curr
                    temp.next = curr.next.next
                    break
                curr = curr.next
        
        return head 
            

            