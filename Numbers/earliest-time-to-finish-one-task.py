

# Problem: earliest-time-to-finish-one-task
# Link: https://leetcode.com/problems/earliest-time-to-finish-one-task/
# Difficulty: Easy
# Approach: Just calculate the time taken for each task and return the minimum time taken










from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        times = [x + y for x, y in tasks]
        return min(times)