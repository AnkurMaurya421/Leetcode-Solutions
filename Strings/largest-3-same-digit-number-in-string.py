
# Problem: largest-3-same-digit-number-in-string
# Link:https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Difficulty: Easy
# Approach: Create a list of all possible 3 same digit combinations from '999' to '000' and check if they are present in the input string.





class Solution:
    def largestGoodInteger(self, num: str) -> str:
        checker=[str(x)*3 for x in range(9,-1,-1)]
        for x in checker:
            if x in num:
                return x
        return ""