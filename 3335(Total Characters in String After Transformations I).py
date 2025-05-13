class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j] = number of characters resulting from transforming chr(i + ord('a')) j times
        # Only need dp[i] for i in 0..25 (for 'a' to 'z')
        dp = [ [0] * (t + 1) for _ in range(26) ]
        
        # Base case: 0 transformations → 1 character
        for c in range(26):
            dp[c][0] = 1
        
        for step in range(1, t + 1):
            for c in range(26):
                if c == 25:
                    # 'z' → "ab"
                    dp[c][step] = (dp[0][step - 1] + dp[1][step - 1]) % MOD
                else:
                    # c → c+1
                    dp[c][step] = dp[c + 1][step - 1]
        
        total = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            total = (total + dp[idx][t]) % MOD
        
        return total


# Copy code by ChatGpt