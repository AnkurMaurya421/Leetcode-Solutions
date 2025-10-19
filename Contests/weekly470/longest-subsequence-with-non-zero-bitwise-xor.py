
# Problem: longest-subsequence-with-non-zero-bitwise-xor
# Link: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
# Difficulty: Medium
# Approach:->use the intuition that xor will be zero if all elements are zero
#->if there are non zero elements and xor is still zero then we have to remove exactly on element to make it non zero





from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        l=len(nums)      
        xor=nums[0]         

        if nums[0]==0:         #checking if first element is zero
            allzero=True
        else:
            allzero=False


        for x in range(1,l):
            xor^=nums[x]
            if nums[x]!=0:
                allzero=False

        if allzero:
            return 0
        if xor==0:
            return l-1
        return l