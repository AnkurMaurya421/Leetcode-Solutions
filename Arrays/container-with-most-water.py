# Problem: container-with-most-water
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Difficulty: Medium
# Approach: Greedy, Two Pointers
#             1) Use two pointers, one at the start and one at the end of the array
#             2) Calculate the area formed by the lines at the two pointers
#             3) Move the pointer pointing to the shorter line towards the other pointer
#             4) Repeat steps 2 and 3 until the two pointers meet
#             5) Keep track of the maximum area found during the process




class Solution:
    def maxArea(self, height: List[int]) -> int:
        r,l,volume,maxVolume=(len(height)-1),0,0,0
        while (l!=r):
            volume=(r-l)*min(height[l],height[r])
            maxVolume=max(maxVolume,volume)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxVolume


            