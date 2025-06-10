from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]

        max_diff = float('-inf')
        for odd in odd_freqs:
            for even in even_freqs:
                max_diff = max(max_diff, odd - even)

        return max_diff

# Copy code in chatpgt
