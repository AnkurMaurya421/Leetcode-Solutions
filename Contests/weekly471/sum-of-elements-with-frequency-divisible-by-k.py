
# Problem: sum-of-elements-with-frequency-divisible-by-k
# Link: https://leetcode.com/contest/weekly-contest-471/problems/sum-of-elements-with-frequency-divisible-by-k/
# Difficulty: Easy
# Approach: Use a dictionary to count the frequency of each element in the array.
#  Then, iterate through the dictionary and for each element whose frequency is divisible by k,
#  add the product of the element and its frequency to the result.


from typing import List




class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        result=0
        for x in dic:
            if dic[x]%k==0:
                result+=(x*dic[x])
        return result