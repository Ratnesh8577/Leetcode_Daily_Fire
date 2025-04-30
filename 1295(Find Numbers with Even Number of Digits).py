class Solution(object):
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            digits = 0
            while num > 0:
                num = num // 10
                digits += 1
            if digits % 2 == 0:
                count += 1
        
        return count



class Solution(object):
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            if num == 0:
                digits = 1
            else:
                digits = 0
                while num > 0:
                    num = num // 10
                    digits += 1
                    
            if digits % 2 == 0:
                count += 1
        
        return count

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
