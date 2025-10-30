

# Problem: sqrtx
# Link: https://leetcode.com/problems/sqrtx/
# Difficulty: Easy
# Approach: Binary search between 0 to x to find the integer square root. If mid*mid is equal to x, return mid. If mid*mid is greater than x, move the right pointer to mid-1. If mid*mid is less than x, update maxi to mid if mid is greater than maxi and move the left pointer to mid+1. Finally, return maxi.

class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        maxi=0
        while(l<=r):
            mid=(l+r)//2
            if (mid*mid)==x:
                return mid
            if (mid*mid)>x:
                r=mid-1
            else:
                if mid>maxi:
                    maxi=mid
                l=mid+1
        return maxi
                