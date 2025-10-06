# Problem: majority-frequency-characters
# Link: https://leetcode.com/problems/majority-frequency-characters/
# Difficulty: Easy
# Approach: 
#            1) Count frequency of each character
#            2) Group characters by their frequency
#            3) then store character by their frequency in a dictionary
#            4) Find the maximum length of characters grouped by frequency
#            5) sort the keys of the dictionary in descending order
#            6) return the characters with the maximum length from the sorted keys

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        charFreq={}
        majorityFreq={}
        for x in s:
            if x in charFreq:
                charFreq[x]+=1
            else:
                charFreq[x]=1
        maxMaj=0
        for x,y in charFreq.items():
            if y not in majorityFreq:
                majorityFreq[y]=x
            else:
                majorityFreq[y]+=x
            maxMaj=max(maxMaj,len(majorityFreq[y]))
        
        keys=sorted(majorityFreq.keys(),reverse=True)
        
        for x in keys:
            
            if len(majorityFreq[x])==maxMaj:
                return majorityFreq[x]
        