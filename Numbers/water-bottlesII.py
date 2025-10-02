# Problem: Water Bottles 2
# Link: https://leetcode.com/problems/water-bottles-ii/
# Difficulty: Medium
# Approach: Just simulate the process on given conditions



class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles=numBottles
        drunkBottles=0
        emptyBottles=0
        while(True):
            emptyBottles+=fullBottles
            drunkBottles+=fullBottles
            fullBottles=0
            if emptyBottles<numExchange:
                return drunkBottles
            else:
                emptyBottles-=numExchange
                numExchange+=1
                fullBottles+=1
        

