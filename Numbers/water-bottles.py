# Problem: Water Bottles
# Link: https://leetcode.com/problems/water-bottles/
# Difficulty: Easy
# Approach: Use simple division and modulus to simulate the process



class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles=numBottles
        drankBottles=0
        emptyBottles=0
        while fullBottles!=0:
            drankBottles+=fullBottles
            emptyBottles+=fullBottles
            fullBottles=emptyBottles//numExchange
            emptyBottles=emptyBottles%numExchange
        return drankBottles