# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Approach: Use hashmap to store seen numbers and find complement


from rpds import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i , num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i