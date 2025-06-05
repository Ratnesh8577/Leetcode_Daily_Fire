class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize each character as its own parent
        parent = [i for i in range(26)]  # for 'a' to 'z'

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function: always attach the larger one to the smaller one
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Step 1: Build equivalence relationships
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Step 2: Build the smallest equivalent string
        result = []
        for ch in baseStr:
            smallest = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)
# Copy code chatgpt