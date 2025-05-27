"""class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_divisible = 0
        divisible = 0
        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                not_divisible += i
        return not_divisible - divisible
"""
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (n*(n+1)>>1) - (sum([i for i in range(1,n+1) if i%m == 0] or [0])<<1)
        