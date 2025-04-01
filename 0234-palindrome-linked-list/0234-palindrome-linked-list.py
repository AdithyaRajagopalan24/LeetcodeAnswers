# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p1, p2, prev = head, head, None
        while p2 and p2.next:
            p1, p2 = p1.next, p2.next.next
        prev, p1, prev.next = p1, p1.next, None
        while p1:
            p1.next, prev, p1 = prev, p1, p1.next
        p2, p1 = head, prev
        while p1:
            if p2.val != p1.val: return False
            p2, p1 = p2.next, p1.next
        return True