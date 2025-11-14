
# Problem: maximum-number-of-operations-to-move-ones-to-the-end
# Link: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
# Difficulty: Medium
# Approach: Use two pointers to track the rightmost zero and iterate through the string counting the number of ones before each zero to calculate the maximum operations.















class Solution:
    def maxOperations(self, s: str) -> int:
        #few funtions to simplify things
        def findEndPoint(s): #checks the last place in string where we can move any 1's for operation
            for x in range(len(s)-1,-1,-1):
                if s[x]=="0":
                    return x
            return None
        #set the right pointer
        r=findEndPoint(s)
        if not r: #means every element is 1
            return 0
        if r==0: #means string is already optimized and no further operations can be performed
            return 0
        
        maxOperations=0 #set the counter
        
        index=0
        ones=False
        currentOneCounter=0
        totalOne=0
        while index<=r: # last 0 is at index r
            if s[index]=="1":
                totalOne+=1  #count total number of ones we have previously seen
                ones=True
            elif ones:
                ones=False             #now we are at zero index and have seen atleast one fresh 1 in 
                maxOperations+=totalOne # now add all previously seen 1 to opertaion sum
            index+=1
        return maxOperations
                
            

            

