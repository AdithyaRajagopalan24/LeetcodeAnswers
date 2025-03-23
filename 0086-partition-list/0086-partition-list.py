class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        prev, next = before, after
        while head:
            if head.val < x:
                prev.next, prev = head, head
            else:
                next.next, next = head, head
            head = head.next
        next.next = None
        prev.next = after.next
        return before.next