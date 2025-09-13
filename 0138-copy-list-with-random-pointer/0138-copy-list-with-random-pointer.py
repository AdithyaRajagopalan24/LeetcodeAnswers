class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapping = {}
        node = head
        while node:
            mapping[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            mapping[node].next = mapping.get(node.next)
            mapping[node].random = mapping.get(node.random)
            node = node.next
        return mapping[head]
