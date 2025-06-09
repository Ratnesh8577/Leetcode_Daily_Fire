class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # since we're starting at 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  # move to next sibling
            else:
                curr *= 10  # move to first child
                k -= 1

        return curr
