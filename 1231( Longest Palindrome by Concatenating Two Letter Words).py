class Solution:
    def longestPalindrome(self, words):
        freq = {}

        # Manually count word frequencies
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        length = 0
        central_used = False

        for word in list(freq.keys()):
            rev = word[::-1]
            if word != rev:
                if rev in freq:
                    pairs = min(freq[word], freq[rev])
                    length += pairs * 4
                    freq[word] -= pairs
                    freq[rev] -= pairs
            else:
                # word is a palindrome like "gg", "aa", etc.
                pairs = freq[word] // 2
                length += pairs * 4
                freq[word] -= pairs * 2

        # Check for one unpaired palindromic word to put in the center
        for word in freq:
            if word[0] == word[1] and freq[word] > 0:
                length += 2
                break

        return length
