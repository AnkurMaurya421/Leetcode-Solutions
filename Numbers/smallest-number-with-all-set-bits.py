# Problem: smallest-number-with-all-set-bits
# Link: https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Difficulty: Easy
# Approach: set bit numbers are of form (2**n)-1. So we can keep on checking for (2**n)-1 until we find the number greater than or equal to num.

class Solution:
    def smallestNumber(self, n: int) -> int:
        x=1
        while True:
            if ((2**x)-1)>=n:
                return ((2**x)-1)
            x+=1
        