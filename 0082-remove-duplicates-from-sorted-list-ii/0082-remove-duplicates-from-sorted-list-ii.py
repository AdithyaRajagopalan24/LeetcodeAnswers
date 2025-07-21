class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy

        while head and head.next:
            if head.val == head.next.val:
                dup = head.val
                while head and head.val == dup:
                    head = head.next
                temp.next = head
            else:
                temp = head
                head = head.next

        return dummy.next