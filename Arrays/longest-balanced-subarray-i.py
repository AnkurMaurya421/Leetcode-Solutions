
# Problem: longest-balanced-subarray-i
# Link: https://leetcode.com/problems/longest-balanced-subarray-i/
# Difficulty: Medium
# Approach: Brute Force: Check all subarrays and count unique even and odd numbers using a set.
#  Update the result if counts are equal.









from rpds import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result=0
        window=0
        current=set()
        odd=0
        even=0
        for x in range(len(nums)):
            window=0
            current=set()
            odd=0
            even=0
            for j in range(x,len(nums)):
                if nums[j]%2==0 and nums[j] not in current:
                    even+=1
                    current.add(nums[j])
                elif nums[j]%2!=0 and nums[j] not in current:
                    odd+=1
                    current.add(nums[j])
                window+=1
                if odd==even:
                    result=max(result,window)
        return result