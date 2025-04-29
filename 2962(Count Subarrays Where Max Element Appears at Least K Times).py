class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        max_val = max(nums)
        result = 0

        count = 0
        left = 0

        for right in range(n):
            if nums[right] == max_val:
                count += 1

            while count >= k:
                result += (n - right)
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return result
