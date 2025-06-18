from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            group = nums[i:i+3]
            if len(group) < 3 or group[2] - group[0] > k:
                return []
            res.append(group)
            i += 3
        return res
