class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        ans = 0
        for num in nums:
            num %= k
            for i in range(k):
                dp[i][num] = dp[num][i] + 1
                ans = max(ans, dp[i][num])
        return ans
      