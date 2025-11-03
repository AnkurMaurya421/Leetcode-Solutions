


# Problem: minimum-time-to-make-rope-colorful
# Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Difficulty: Medium
# Approach: greedy approach, iterate through the rope and whenever two adjacent colors are the same, remove the one with the smaller cost
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=0
        time=0
        for current in range(1,len(colors)):
            if colors[current]==colors[prev]:
                if neededTime[current]<neededTime[prev]:
                    time+=neededTime[current]
                else:
                    time+=neededTime[prev]
                    prev=current
            else:
                prev=current
        return time
                