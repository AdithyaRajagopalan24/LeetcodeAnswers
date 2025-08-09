class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        all_sequences = set()

        def backtrack(word, visited):
            for i in range(len(tiles)):
                if visited[i]:
                    continue
                char_sequence = word + tiles[i]
                visited[i] = True
                all_sequences.add(char_sequence)
                backtrack(char_sequence, visited)
                visited[i] = False

        backtrack("", [False] * len(tiles))
        return len(all_sequences)