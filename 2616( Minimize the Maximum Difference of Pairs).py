from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        # Helper function to check if we can form at least p pairs with max difference <= max_diff
        def canFormPairs(max_diff: int) -> bool:
            i = 0
            count = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip both indices to prevent reuse
                else:
                    i += 1
            return count >= p

        low, high = 0, nums[-1] - nums[0]
        result = high

        while low <= high:
            mid = (low + high) // 2
            if canFormPairs(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
# Copy code chatgpt
