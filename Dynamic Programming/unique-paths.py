# Problem: unique-paths
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium
# Approach: Use a Dp approact with memoization to store the number of unique paths to each cell.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def recur(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            if m==1 and n==1:
                return 1
            if m<1 or n<1:
                return 0
            memo[(m,n)] =recur(m,n-1)+recur(m-1,n)
            return memo[(m,n)]
        return recur(m,n)