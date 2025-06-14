class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Generate max by replacing the first non-9 digit with 9
        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))
                break
        else:
            max_num = num  # already all 9s

        # Generate min by replacing the first non-0 digit with 0
        for d in s:
            if d != '0':
                min_num = int(s.replace(d, '0'))
                break
        else:
            min_num = num  # already all 0s

        return max_num - min_num
#Copy code chatgpt