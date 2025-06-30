from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)  # Count frequency of each number
        max_length = 0

        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])

        return max_length
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # Move left pointer until the window is valid (diff <= 1)
            while nums[right] - nums[left] > 1:
                left += 1
            # Check if diff == 1, update max_len
            if nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)

        return max_len
