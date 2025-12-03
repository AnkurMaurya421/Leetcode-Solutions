

# Problem: binary-search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Approach: Basic binary search algorithm implementation
from typing import List







class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #basic binary search algo implementation
        left=0
        right=len(nums)-1
        while left<=right:

            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        return -1
