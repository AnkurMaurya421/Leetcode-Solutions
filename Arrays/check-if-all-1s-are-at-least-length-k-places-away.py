


# Problem: Check if All 1's Are at Least Length K Places Away
# Link: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Difficulty: Easy
# Approach: Iterating through the array and counting zeros between 1s









class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag=False
        counter=0
        for x in nums:
            if flag:
                if x==0:
                    counter+=1
                if x==1:
                    if counter<k:
                        return False
                    counter=0
            if x==1:
                flag=True
        return True

        