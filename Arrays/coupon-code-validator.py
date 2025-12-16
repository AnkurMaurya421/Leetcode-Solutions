

# Problem: coupon-code-validator
# Link: https://leetcode.com/problems/coupon-code-validator/
# Difficulty: Easy
# Approach: Sorting and Validation
#             1) Validate each coupon code based on given criteria
from typing import List








class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
        n=len(code)
        
        businessline=["electronics","grocery","pharmacy","restaurant"]
        def checkcode(code):
            result=True
            for c in code:
                if c not in s:
                    return False
            return True
        def checkbusiness(business):
            if business in businessline:
                return True
            return False
        result=[]
        for business in businessline:
            temp=[]
            for x in range(n):
                if checkcode(code[x]) and businessLine[x]==business and isActive[x] and code[x]:
                    temp.append(code[x])
                    
            temp.sort()
            
            result=result+temp
        return result