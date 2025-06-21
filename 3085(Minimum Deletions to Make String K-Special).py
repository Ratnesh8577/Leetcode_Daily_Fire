class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter

        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        prefix_sum = [0] * (n + 1)

        # Precompute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + freq[i]

        res = float('inf')

        # Try each freq[i] as lower bound
        for i in range(n):
            low = freq[i]
            high = low + k

            # Delete all characters with freq < low (i elements)
            delete_left = prefix_sum[i]

            # Delete characters with freq > high
            # Find first index where freq > high
            l, r = i, n
            while l < r:
                m = (l + r) // 2
                if freq[m] > high:
                    r = m
                else:
                    l = m + 1
            # l is the first index with freq > high
            delete_right = sum(freq[l:]) - (high * (n - l))

            total_deletes = delete_left + delete_right
            res = min(res, total_deletes)

        return res
# Copy code in chatgpt
