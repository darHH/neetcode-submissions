# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 and list1.val <= list2.val:
            start = list1
            curr = start
            list1 = list1.next
        elif list1 and list2 and list1.val > list2.val:
            start = list2
            curr = start
            list2 = list2.next
        elif list1 and not list2:
            return list1
        else:
            return list2
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp = list1.next
                curr.next = list1
                curr = curr.next 
                list1 = temp
            else:
                temp = list2.next
                curr.next = list2
                curr = curr.next
                list2 = temp
        if list1 != None:
            curr.next = list1
        elif list2 != None:
            curr.next = list2
        return start
        
            
