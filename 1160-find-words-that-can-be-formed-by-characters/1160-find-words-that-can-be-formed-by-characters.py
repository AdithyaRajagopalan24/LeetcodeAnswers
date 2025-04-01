class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        for word in words:
            for letter in word:
                if word.count(letter)>chars.count(letter):
                    break
            else:
                count+=len(word)
        
        return count