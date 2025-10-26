# Problem: remove-zeros-in-decimal-representation
# Link: https://leetcode.com/problems/remove-zeros-in-decimal-representation/
# Difficulty: Easy
# Approach: convert number to string and iterate through each character..add non zero characters to result string..finally convert result string to integer and return




class Solution:
    def removeZeros(self, n: int) -> int:
        s=str(n)
        result=""
        for x in s:
            if x!="0":
                result+=x
        return int(result)