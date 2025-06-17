MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        fact, inv_fact = self.get_fact_and_inv_fact(n)

        return m * self.mod_pow(m - 1, n - k - 1) % MOD * self.nCk(n - 1, k, fact, inv_fact) % MOD

    def mod_pow(self, x: int, n: int) -> int:
        result = 1
        x %= MOD
        while n > 0:
            if n % 2:
                result = result * x % MOD
            x = x * x % MOD
            n //= 2
        return result

    def get_fact_and_inv_fact(self, n: int):
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        for i in range(2, n + 1):
            inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
            inv_fact[i] = inv_fact[i - 1] * inv[i] % MOD

        return fact, inv_fact

    def nCk(self, n: int, k: int, fact, inv_fact) -> int:
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
# Copy code Chatgpt