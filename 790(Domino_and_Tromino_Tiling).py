class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        # Let dp[i] be the number of ways to tile a 2 x i board
        dp0, dp1, dp2 = 1, 2, 5  # dp[1]=1, dp[2]=2, dp[3]=5

        for i in range(4, n + 1):
            dp = (2 * dp2 + dp0) % MOD
            dp0, dp1, dp2 = dp1, dp2, dp

        return dp2

        