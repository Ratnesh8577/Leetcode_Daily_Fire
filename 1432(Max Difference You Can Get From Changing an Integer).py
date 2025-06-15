class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Step 1: Maximize 'a' by replacing the first digit that is not '9' with '9'
        for ch in s:
            if ch != '9':
                a = int(s.replace(ch, '9'))
                break
        else:
            a = num  # If all digits are already '9'

        # Step 2: Minimize 'b'
        if s[0] != '1':
            # Replace the first digit with '1' to avoid leading zeros
            b = int(s.replace(s[0], '1'))
        else:
            # Try to replace another digit (not '0' or '1') with '0'
            for ch in s[1:]:
                if ch not in ('0', '1'):
                    b = int(s.replace(ch, '0'))
                    break
            else:
                b = num  # If no eligible digit found

        return a - b
# Copy code chatgpt