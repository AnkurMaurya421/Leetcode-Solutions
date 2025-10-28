# Problem: make-array-elements-equal-to-zero
# Link: https://leetcode.com/problems/make-array-elements-equal-to-zero/description/
# Difficulty: Easy
# Approach: if all elements are zero, each element can be removed in two ways (left or right), so return 2*n
#             1) Calculate the total sum of the array
#             2) Iterate through the array, maintaining left and right sums and checking conditions for valid removals
                #if leftsum == rightsum, the element can be removed from either side (2 ways)
                #if abs(leftsum - rightsum) == 1, the element can be removed from one side (1 way)
from typing import List







class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        rightsum=sum(nums)
        if set(nums)=={0}:
            return len(nums)*2
        leftsum=0
        validSelection=0
        for x in range(len(nums)):
            if nums[x]==0:
                if abs(rightsum-leftsum)==1:
                    validSelection+=1
                elif rightsum==leftsum:
                    if x==len(nums)-1 or x==0:
                        validSelection+=1
                    else:
                        validSelection+=2
            leftsum+=nums[x]
            rightsum-=nums[x]
        return validSelection
        
        