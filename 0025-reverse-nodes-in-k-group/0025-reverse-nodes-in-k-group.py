class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        while count >= k:
            curr = prev.next
            nxt = curr.next
            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
            count -= k
        return dummy.next