



# Problem: jump-game
# Link: https://leetcode.com/problems/jump-game/
# Difficulty: Medium
# Approach: Use a greedy approach to track the maximum reachable index at each step.





from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas=0
        for n in nums:
            if gas<0:
                return False
            if n>gas:
                gas=n
            gas-=1
        return True