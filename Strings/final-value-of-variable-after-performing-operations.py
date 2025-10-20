# Problem: final-value-of-variable-after-performing-operations
# Link:https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty: Easy
# Approach:set x=0 and perform the operation on given condition






from rpds import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for operation in operations:
            if operation in ["X++","++X"]:
                x+=1
            else:
                x-=1
        return x