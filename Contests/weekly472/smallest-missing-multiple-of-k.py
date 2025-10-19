
# Problem: smallest-missing-multiple-of-k
# Link: https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Difficulty: Easy
# Approach: Generate multiples of k and check which is the smallest not present in the array.








from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=[]
        for x in range(1,102):
            s.append(k*x)
        nums=set(nums)
        for x in s:
            if x not in nums:
                return x
        
            
            