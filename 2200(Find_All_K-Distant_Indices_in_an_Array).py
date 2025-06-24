class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = set()
        for j in range(len(nums)):
            if nums[j] == key:
                # Mark all indices i such that |i - j| <= k
                start = max(0, j - k)
                end = min(len(nums) - 1, j + k)
                for i in range(start, end + 1):
                    result.add(i)
        return sorted(result)
