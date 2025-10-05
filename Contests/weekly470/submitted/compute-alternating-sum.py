# Problem: Compute Alternating Sum
# Link: https://leetcode.com/contest/weekly-contest-470/problems/compute-alternating-sum/
# Difficulty: Easy
# Approach: simulate the process of alternating sum by using a boolean flag to track addition and subtraction



class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result=0
        plus=True
        for x in nums:
            if plus :
                result+=x
                plus=False
            else:
                result-=x
                plus=True
        return result