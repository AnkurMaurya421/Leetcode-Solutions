# Problem: Concatenation of Array
# Link: https://leetcode.com/problems/concatenation-of-array/
# Difficulty: Easy
# Approach: Just extend the array with itself


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return nums + nums