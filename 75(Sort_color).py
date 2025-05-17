"""class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

""" 
""" 
2nd method
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
"""
# 3rd Method
class Solution:
    def sortColors(self, nums):
        count0 = count1 = count2 = 0

        # First pass: count
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Second pass: overwrite
        index = 0
        for _ in range(count0):
            nums[index] = 0
            index += 1
        for _ in range(count1):
            nums[index] = 1
            index += 1
        for _ in range(count2):
            nums[index] = 2
            index += 1


# 4th method            
class Solution:
    def sortColors(self, nums):
        insert_pos = 0

        # First pass: move all 0s to the front
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[insert_pos] = 0
                insert_pos += 1

        # Second pass: move all 1s after the 0s
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[insert_pos] = 1
                insert_pos += 1

        # Third pass: fill the rest with 2s
        while insert_pos < len(nums):
            nums[insert_pos] = 2
            insert_pos += 1

# 5th method

class Solution:
    def sortColors(self, nums):
        zeros = []
        ones = []
        twos = []

        # Separate values into three lists
        for num in nums:
            if num == 0:
                zeros.append(0)
            elif num == 1:
                ones.append(1)
            else:
                twos.append(2)

        # Combine them and overwrite original list
        sorted_list = zeros + ones + twos
        for i in range(len(nums)):
            nums[i] = sorted_list[i]

