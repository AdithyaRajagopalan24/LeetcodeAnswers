# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstpointer = head
        second_pointer = head
        while second_pointer and second_pointer.next:
            firstpointer = firstpointer.next
            second_pointer = second_pointer.next.next
            if firstpointer == second_pointer:
                return True
        return False