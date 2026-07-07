from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        q = deque([root])
        ans = []

        while q:
            node = q.popleft()

            if node is None:
                ans.append("n")
                continue

            ans.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return " ".join(ans)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split()
        root = TreeNode(int(values[0]))
        q = deque([root])

        pos = 1

        while q and pos < len(values):
            curr = q.popleft()

            if values[pos] != "n":
                curr.left = TreeNode(int(values[pos]))
                q.append(curr.left)
            pos += 1

            if pos < len(values) and values[pos] != "n":
                curr.right = TreeNode(int(values[pos]))
                q.append(curr.right)
            pos += 1

        return root