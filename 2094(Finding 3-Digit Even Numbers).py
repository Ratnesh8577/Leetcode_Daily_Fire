"""class Solution:
    def findEvenNumbers(self, digits):
        result = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    a, b, c = digits[i], digits[j], digits[k]
                    if a != 0 and c % 2 == 0:
                        number = a * 100 + b * 10 + c
                        result.add(number)

        return sorted(result)
"""

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        ans = []
        c = Counter(digits)
        for i in range(100, 1000, 2):
            dc = Counter(list(str(i)))
            for d in dc:
                if int(d) not in c or c[int(d)] < dc[d]:
                    break
            else:
                ans.append(i)
        return ans
    
# Copy code in ChatGpt