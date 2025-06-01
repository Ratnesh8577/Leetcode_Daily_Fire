"""from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Compute number of non-negative integer solutions to a + b + c = total
        def ways(total):
            return comb(total + 2, 2) if total >= 0 else 0

        # Count number of invalid cases where one child gets > limit
        def subtract_1(n, l):
            return ways(n - l - 1)

        # Two children > limit
        def subtract_2(n, l):
            return ways(n - 2 * (l + 1))

        # All three > limit
        def subtract_3(n, l):
            return ways(n - 3 * (l + 1))

        total = ways(n)
        over1 = 3 * subtract_1(n, limit)
        over2 = 3 * subtract_2(n, limit)
        over3 = subtract_3(n, limit)

        return total - over1 + over2 - over3
"""
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res

        def ways(total):
            return comb(total + 2, 2) if total >= 0 else 0

        def subtract_1(n, l):
            return ways(n - l - 1)

        def subtract_2(n, l):
            return ways(n - 2 * (l + 1))

        def subtract_3(n, l):
            return ways(n - 3 * (l + 1))

        total = ways(n)
        over1 = 3 * subtract_1(n, limit)
        over2 = 3 * subtract_2(n, limit)
        over3 = subtract_3(n, limit)

        return total - over1 + over2 - over3

#Copy code in Chatgpt
