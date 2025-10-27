
# Problem: Number of Laser Beams in a Bank
# Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# Difficulty: Medium
# Approach:  #basically number of beams between two subsequent rows containing device will be product of sum of devices of each row













from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
       
        prevDevices=0
        beams=0

        for row in bank:
            devices=row.count("1")
            if devices>0:
                beams+=prevDevices*(devices)
                prevDevices=devices
            
        return beams