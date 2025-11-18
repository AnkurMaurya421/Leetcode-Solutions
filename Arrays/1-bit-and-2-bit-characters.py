# Problem: 1-bit and 2-bit Characters
# Link: https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Difficulty: Easy
# Approach: Check the last two bits and iterate through the array to determine if the last character is a 1-bit character or not







class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1:
            return True
        if bits[-2]==0:
            return True

        i=0
        while i<len(bits)-1:
            if bits[i]==0:
                i+=1
            else:
                i+=2
        if i==len(bits):
            return False
        return True

             