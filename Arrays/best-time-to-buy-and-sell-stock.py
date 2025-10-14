
# Problem: best-time-to-buy-and-sell-stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Approach: set max and min to the first element of the array
#           set result to 0
#           iterate through the array 
#           if the current element is greater than max, update max
#          if the current element is less than min, update result with max-min 
#         and set min and max to the current element
#        at the end of the loop, update result with max-min
#       return result            

from typing import List







class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax=prices[0]
        currentMin=prices[0]
        result=0
        for x in range(1,len(prices)):
            
            if prices[x]>currentMax:
                currentMax=prices[x]
                
            elif prices[x]<currentMin:
                result=max(result,(currentMax-currentMin))
                
                currentMin,currentMax=prices[x],prices[x]
            
        result=max(result,(currentMax-currentMin))
        return result