class Solution:
    MOD = 10**9 + 7

    def countBalancedPermutations(self, num: str) -> int:
        nums = [int(c) for c in num]
        total = sum(nums)
        if total % 2 == 1:
            return 0

        nums.sort(reverse=True)

        even = (len(nums) + 1) // 2
        odd = len(nums) // 2
        even_balance = total // 2

        # 3D memoization array
        mem = [[[-1 for _ in range(even_balance + 1)] for _ in range(odd + 1)] for _ in range(even + 1)]
        perm = self.get_perm(nums)
        count = self.dfs(nums, even, odd, even_balance, mem)
        return count * self.mod_inverse(perm) % self.MOD

    def dfs(self, nums, even, odd, even_balance, mem):
        if even_balance < 0:
            return 0
        if even == 0:
            return self.factorial(odd) if even_balance == 0 else 0
        idx = len(nums) - (even + odd)
        if odd == 0:
            remaining_sum = sum(nums[idx:])
            return self.factorial(even) if remaining_sum == even_balance else 0
        if mem[even][odd][even_balance] != -1:
            return mem[even][odd][even_balance]
        
        place_even = self.dfs(nums, even - 1, odd, even_balance - nums[idx], mem) * even % self.MOD
        place_odd = self.dfs(nums, even, odd - 1, even_balance, mem) * odd % self.MOD

        mem[even][odd][even_balance] = (place_even + place_odd) % self.MOD
        return mem[even][odd][even_balance]

    def get_perm(self, nums):
        count = [0] * 10
        for digit in nums:
            count[digit] += 1

        res = 1
        for freq in count:
            res = res * self.factorial(freq) % self.MOD
        return res

    def factorial(self, n):
        res = 1
        for i in range(2, n + 1):
            res = res * i % self.MOD
        return res

    def mod_inverse(self, a):
        m = self.MOD
        y, x = 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x, y = y, x - q * y
        return x + self.MOD if x < 0 else x
