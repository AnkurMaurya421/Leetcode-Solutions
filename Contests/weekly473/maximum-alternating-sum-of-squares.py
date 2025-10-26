
# Problem: maximum-alternating-sum-of-squares
# Link: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Difficulty: Medium
# Approach: convert each element to its square and then sort the array...half of the elements at negative positions should be the smallest
# for max alternating sum..so sum the smaller half as negative and larger half as positive and return the result






from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[(abs(x))**2 for x in nums]
        nums.sort()
        negElem=len(nums)//2
        neg=sum(nums[:negElem])
        pos=sum(nums[negElem:])
        return pos-neg
        
        
            