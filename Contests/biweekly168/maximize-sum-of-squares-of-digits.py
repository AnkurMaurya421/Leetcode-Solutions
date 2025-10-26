

# Problem: maximize-sum-of-squares-of-digits
# Link: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Difficulty: Medium
# Approach: calculate how many 9's can fit in the sum and check for remainder..if remainder exists we need one more digit.
# .check if total digits needed is less than or equal to num..if yes construct the number with 9's , remainder and 0's else return empty string





class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        minBox=0
        flag=0
        mod=sum%9
        div=sum//9
        if mod>0:
            flag=1
        minBox=flag+div
        if minBox>num:
            return ""
        else:
            if mod>0:
                return ("9"*div)+str(mod)+("0"*(num-minBox))
            else:
                return ("9"*div)+("0"*(num-minBox))
        