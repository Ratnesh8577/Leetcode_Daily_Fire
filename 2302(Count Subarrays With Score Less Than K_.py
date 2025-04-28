class Solution(object):
    def countSubarrays(self, nums, k):

        n = len(nums)
        left = 0
        total = 0
        result = 0

        for right in range(n):

            total += nums[right]
        
            while left <= right and total * (right - left + 1) >= k:


                total -= nums[left]
                left += 1
        
            result += (right - left + 1)
    
        return result
        
        

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        