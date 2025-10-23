
# Problem: check-if-digits-are-equal-in-string-after-operations-i
# Link:https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
# Difficulty: Easy
# Approach:create a funtion for the given operation so that we can repeatedly call it until the length of string is 2. finally check if both digits are equal or not.








class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def operation(s):
            li=[int(x) for x in s]
            result=[]
            for x in range(len(s)-1):
                result.append(str((li[x]+li[x+1])%10))
            return "".join(result)
        
        while len(s)>2:
            s=operation(s)
           
        if s[0]==s[1]:
            return True
        return False
                
            