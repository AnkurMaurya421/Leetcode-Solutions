

# Problem: count-elements-with-maximum-frequency
# Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Difficulty: Easy
# Approach: Hash Map
#             1) Use a hash map to count the frequency of each element in the array 

from typing import List






class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic={}
        maxFreq=0
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
            maxFreq=max(maxFreq,dic[x])
        result=0
        for x in dic:
            if dic[x]==maxFreq:
                result+=maxFreq
        return result