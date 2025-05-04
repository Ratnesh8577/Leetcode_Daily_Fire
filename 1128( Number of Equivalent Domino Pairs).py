class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = {}
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            if key in count:
                result += count[key]
                count[key] += 1
            else:
                count[key] = 1

        return result
