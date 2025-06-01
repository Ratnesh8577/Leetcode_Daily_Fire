"""
class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n
        for i in range(n):
            nums[i] //= n
        return nums

"""

class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        ans=[0]*n
        for i in range(0,n):
            ans[i]=nums[nums[i]]
        return ans

# Best Method

