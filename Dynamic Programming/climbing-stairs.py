


# Problem: climbing-stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Approach: Use recursion with memoization to avoid recomputation of already solved subproblems.
#  The number of ways to reach the nth step is the sum of the ways to reach the (n-1)th and (n-2)th steps.





class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(n,memo):
            if n in memo:
                return memo[n]
            if n==0:
                return 1
            if n==-1:
                return 0
            result=recur(n-1,memo)+recur(n-2,memo)
            memo[n]=result
            return memo[n]
        return recur(n,{})