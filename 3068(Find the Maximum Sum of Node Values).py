from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        gains = [(num ^ k) - num for num in nums]

        total_gain = 0
        min_abs_gain = float('inf')
        count = 0

        for gain in gains:
            if gain > 0:
                total_gain += gain
                count += 1
            min_abs_gain = min(min_abs_gain, abs(gain))

        # We can flip an even number of nodes
        if count % 2 == 0:
            return total + total_gain
        else:
            return total + total_gain - min_abs_gain
# copy code chatgpt