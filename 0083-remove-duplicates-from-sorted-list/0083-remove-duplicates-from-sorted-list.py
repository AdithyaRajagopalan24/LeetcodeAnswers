# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
    
        current = head
        while current.next:
            check = current.next
            if current.val == check.val:
                current.next = check.next
            else:
                current = check
    
        return head
