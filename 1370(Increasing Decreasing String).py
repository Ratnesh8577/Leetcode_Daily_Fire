class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26  # Frequency array for 'a' to 'z'

        for ch in s:
            freq[ord(ch) - ord('a')] += 1  # Count frequency

        result = []
        total = len(s)

        while len(result) < total:
            # Step 1-3: Increasing order
            for i in range(26):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

            # Step 4-6: Decreasing order
            for i in range(25, -1, -1):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

        return ''.join(result)

# Hard question Copy chatgpt
