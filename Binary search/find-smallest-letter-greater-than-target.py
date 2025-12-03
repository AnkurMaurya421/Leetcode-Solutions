


# Problem: find-smallest-letter-greater-than-target
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Difficulty: Easy
# Approach: Basic binary search algorithm implementation to find the smallest letter greater than the target. Initialize left and right pointers, and a variable to store the current greatest letter found. Update the pointers based on comparisons and finally return the smallest letter greater than the target.
from typing import List




class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        greater=letters[0]
        while l<=r:
            mid=(l+r)//2
            if letters[mid]>target:
                greater=letters[mid]
                r=mid-1
            else:
                l=mid+1
        return greater
