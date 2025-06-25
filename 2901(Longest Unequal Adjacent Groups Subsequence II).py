from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        def hamming_distance(s1: str, s2: str) -> int:
            # Assumes s1 and s2 have same length
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        dp = [1] * n           # dp[i] = length of longest subsequence ending at i
        prev = [-1] * n        # prev[i] = previous index in subsequence ending at i
        
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_distance(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        # Find the index with the maximum dp value
        max_index = max(range(n), key=lambda i: dp[i])
        
        # Reconstruct subsequence
        res = []
        while max_index != -1:
            res.append(words[max_index])
            max_index = prev[max_index]
        
        return res[::-1]

# Copy code in chatgpt
