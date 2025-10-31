
# Problem: the-two-sneaky-numbers-of-digitville
# Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Difficulty: Easy
# Approach: use set to track seen numbers, if a number is seen again, it's one of the sneaky numbers
from typing import List







class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        #use set
        check=set()
        result=[]
        for x in nums:
            if x in check:
                result.append(x)
                continue
            check.add(x)
        return result