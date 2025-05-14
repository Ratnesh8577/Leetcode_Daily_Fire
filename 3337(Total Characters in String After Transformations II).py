from typing import List

MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        size = 26

        # Build the transition matrix
        T = [[0] * size for _ in range(size)]
        for i in range(size):
            start = (i + 1) % size
            for j in range(nums[i]):
                T[i][(start + j) % size] += 1

        # Matrix exponentiation
        def mat_mult(a, b):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if a[i][k] == 0:
                        continue
                    for j in range(size):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            result = [[int(i == j) for j in range(size)] for i in range(size)]  # Identity matrix
            while power:
                if power % 2 == 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result

        T_pow = mat_pow(T, t)

        # Initial count vector for s
        initial = [0] * size
        for ch in s:
            initial[ord(ch) - ord('a')] += 1

        # Multiply initial vector by matrix T^t
        result = 0
        for i in range(size):
            for j in range(size):
                result = (result + initial[i] * T_pow[i][j]) % MOD

        return result
