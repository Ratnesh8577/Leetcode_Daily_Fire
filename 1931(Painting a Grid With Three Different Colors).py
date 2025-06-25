"""class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from functools import lru_cache

        MOD = 10**9 + 7
        colors = [0, 1, 2]  # Red, Green, Blue

        # Step 1: Generate all valid column colorings
        def generate_valid_columns():
            result = []

            def backtrack(path):
                if len(path) == m:
                    result.append(tuple(path))
                    return
                for color in colors:
                    if not path or path[-1] != color:
                        backtrack(path + [color])

            backtrack([])
            return result

        valid_columns = generate_valid_columns()

        # Step 2: Build transition map between valid column colorings
        transitions = {}
        for c1 in valid_columns:
            transitions[c1] = []
            for c2 in valid_columns:
                if all(a != b for a, b in zip(c1, c2)):
                    transitions[c1].append(c2)

        # Step 3: DP initialization
        dp = {c: 1 for c in valid_columns}

        # Step 4: Fill DP table for all n columns
        for _ in range(n - 1):
            new_dp = {}
            for c1 in valid_columns:
                new_dp[c1] = 0
                for c2 in transitions[c1]:
                    new_dp[c1] = (new_dp[c1] + dp[c2]) % MOD
            dp = new_dp

        # Step 5: Sum all possible colorings for the last column
        return sum(dp.values()) % MOD
"""

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        from itertools import product

        # Step 1: Generate all valid column colorings as integers
        def is_valid(col):
            for i in range(1, len(col)):
                if col[i] == col[i - 1]:
                    return False
            return True

        def encode(col):
            # convert list like [0,1,2] into a single int like 012 base-3
            res = 0
            for c in col:
                res = res * 3 + c
            return res

        def decode(code):
            # convert int code to list of base-3 digits
            col = []
            for _ in range(m):
                col.append(code % 3)
                code //= 3
            return col[::-1]

        all_cols = []
        for prod in product(range(3), repeat=m):
            if is_valid(prod):
                all_cols.append(encode(prod))

        # Step 2: Precompute valid transitions
        transitions = {}
        for c1 in all_cols:
            t1 = []
            col1 = decode(c1)
            for c2 in all_cols:
                col2 = decode(c2)
                if all(a != b for a, b in zip(col1, col2)):
                    t1.append(c2)
            transitions[c1] = t1

        # Step 3: Initialize DP
        dp = {c: 1 for c in all_cols}

        # Step 4: Iterate over columns
        for _ in range(n - 1):
            new_dp = {c: 0 for c in all_cols}
            for c1 in all_cols:
                for c2 in transitions[c1]:
                    new_dp[c2] = (new_dp[c2] + dp[c1]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
    # Copy code in chatgpt
