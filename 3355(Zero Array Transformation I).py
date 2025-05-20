class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        delta = [0] * (n + 1)

        # Mark range increments in delta
        for l, r in queries:
            delta[l] += 1
            if r + 1 < len(delta):
                delta[r + 1] -= 1

        # Compute prefix sum to get coverage count at each index
        coverage = [0] * n
        curr = 0
        for i in range(n):
            curr += delta[i]
            coverage[i] = curr

        # Check if nums[i] can be decremented using available queries
        for i in range(n):
            if nums[i] > coverage[i]:
                return False

        return True
