from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)     # Count frequency of each character in s
        t = []                 # Stack for characters held by robot
        result = []            # Final string to write on paper
        min_char = 'a'         # Track current smallest character in s

        for ch in s:
            t.append(ch)       # Operation 1: Move from s to t
            count[ch] -= 1     # Decrease count of ch in s
            
            # Update min_char to the next smallest character still available
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            # Operation 2: Write from t to result if it's <= remaining smallest in s
            while t and t[-1] <= min_char:
                result.append(t.pop())

        # Append remaining characters in t to result
        while t:
            result.append(t.pop())

        return ''.join(result)
# Copy code in chatgpt