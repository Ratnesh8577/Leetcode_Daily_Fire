from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each number with its index
        indexed = list(enumerate(nums))  # [(index, value)]

        # Step 2: Get top k elements by value (descending order)
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]

        # Step 3: Sort those k elements by their original index to preserve order
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[0])

        # Step 4: Extract values to form the subsequence
        return [val for idx, val in top_k_sorted_by_index]
