class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        mid, end = head, head
        while end and end.next:
            mid = mid.next
            end = end.next.next

        prev, curr = None, mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        left, right = head, prev
        while right.next:
            lNext, rNext = left.next, right.next
            left.next = right
            right.next = lNext
            left, right = lNext, rNext
