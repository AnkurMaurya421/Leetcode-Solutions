


# Problem: lexicographically-smallest-string-after-reverse
# Link: https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/
# Difficulty: Medium
# Approach: check all possible reversals by iterating through each index and reversing the substring from start to that index and from that index to end..keep track of smallest string and return it

from typing import List







class Solution:
    def lexSmallest(self, s: str) -> str:
        smallest=s
        for x in range(1,len(s)+1):
            s1=(s[:x])[::-1]+s[x:]
            s2=(s[:-x] + s[-x:][::-1] if x <= len(s) else s[::-1])
            smallest=min(smallest,s1)
            smallest=min(smallest,s2)
            
        
        return smallest