




# Problem: find-n-unique-integers-sum-up-to-zero
# Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Difficulty: Easy
# Approach: We can pair positive and negative integers to sum up to zero. If n is odd, we can include zero as well.






from rpds import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        result=[]
        for x in range(1,n//2+1):
            result.append(x)
            result.append(-x)
        if n%2==0:
            return result
        result.append(0)
        return result
            