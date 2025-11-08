
# Problem: find-missing-elements

# Link: https://leetcode.com/problems/find-missing-elements/description/
# Difficulty: Easy
# Approach: Iterate through the range from the minimum to the maximum element in the array
#             and check for each number if it is present in the array









from rpds import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = min(nums)
        nums=set(nums)
        result=[]
        for x in range(mini+1,maxi):
            if x not in nums:
                result.append(x)
        return result