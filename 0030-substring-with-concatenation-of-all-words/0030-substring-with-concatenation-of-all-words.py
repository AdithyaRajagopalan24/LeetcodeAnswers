from collections import Counter, defaultdict


class Solution:
	"""
	Time:   O(n*k), n = length of s, k = length of each word
	Memory: O(m*k), m = length of words, k = length of each word
	"""

	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		length = len(words[0])
		word_count = Counter(words)
		indexes = []
		for i in range(length):
			start = i
			window = defaultdict(int)
			wordsUsedUp = 0
			for j in range(i, len(s) - length + 1, length):
				word = s[j:j + length]
				if word not in word_count:
					start = j + length
					window = defaultdict(int)
					wordsUsedUp = 0
					continue
				wordsUsedUp += 1
				window[word] += 1
				while window[word] > word_count[word]:
					window[s[start:start + length]] -= 1
					start += length
					wordsUsedUp -= 1
				if wordsUsedUp == len(words):
					indexes.append(start)
		return indexes