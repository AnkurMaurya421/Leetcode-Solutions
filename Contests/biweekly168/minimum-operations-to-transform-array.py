

# Problem: minimum-operations-to-transform-array
# Link: https://leetcode.com/problems/minimum-operations-to-transform-array/
# Difficulty: Medium
# Approach: check if last element of nums2 can be achieved by minimum zero oepration...calculate the difference between corresponding elements of nums1 and nums2..sum the absolute differences
# ..finally add minimum operations needed to achieve last element of nums2 from any element of nums1


from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        result=0
        toappend=nums1[0]
        mini=max(max(nums2),max(nums1))
        for x in range(len(nums1)):
            mini=min(mini,abs(nums1[x]-nums2[-1]))
            mini=min(mini,abs(nums2[x]-nums2[-1]))
            greater=max(nums1[x],nums2[x])
            minor=min(nums1[x],nums2[x])
            if nums2[-1]<=greater and nums2[-1]>=minor:
                mini=0
            
        for j in range(len(nums1)):
            result+=(abs(nums1[j]-nums2[j]))
        return result+mini+1