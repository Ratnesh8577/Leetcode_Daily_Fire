from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0

        for i in range(n):
            # Use modulo to wrap around the circular array
            diff = abs(nums[i] - nums[(i + 1) % n])
            max_diff = max(max_diff, diff)

        return max_diff
