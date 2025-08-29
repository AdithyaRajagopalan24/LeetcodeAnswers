class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node):
            letter = board[r][c]
            nxt = node[letter]
            word = nxt.pop('#', None)
            if word:
                results.append(word)

            board[r][c] = '*'  
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in nxt:
                    dfs(nr, nc, nxt)
            board[r][c] = letter  

            if not nxt:
                node.pop(letter)

        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word

        rows, cols = len(board), len(board[0])
        results = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return results
