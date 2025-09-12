class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle, fastPointer = head, head.next
        while fastPointer and fastPointer.next:
            middle, fastPointer = middle.next, fastPointer.next.next
        
        rightHalf, middle.next = middle.next, None
        leftSorted = self.sortList(head)
        rightSorted = self.sortList(rightHalf)
        
        return self.mergeLists(leftSorted, rightSorted)
    
    def mergeLists(self, listA: Optional[ListNode], listB: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = current = ListNode()
        while listA and listB:
            if listA.val < listB.val:
                current.next, listA = listA, listA.next
            else:
                current.next, listB = listB, listB.next
            current = current.next
        current.next = listA or listB
        return dummyHead.next
