class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1  # We need at least one subsequence
        start = 0  # Start index of the current group

        for i in range(len(nums)):
            if nums[i] - nums[start] > k:
                count += 1
                start = i  # Start a new group from this index

        return count
