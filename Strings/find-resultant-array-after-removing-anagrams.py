# Problem: find-resultant-array-after-removing-anagrams
# Link:https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# Difficulty: Easy
# Approach: create a funtion to check anagram and then iterate through the array
#  using a pointer to check if the current word is an anagram of the previous word.
#  If it is not an anagram, add it to the result array.











from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def checkAnagram(s1,s2):
            if len(s1)!=len(s2):
                return False
            count={}
            for char in s1:
                if char in count:
                    count[char]+=1
                else:
                    count[char]=1
            for char in s2:
                if char in count:
                    count[char]-=1
                else:
                    return False
            for key in count:
                if count[key]!=0:
                    return False
            return True
        result=[]
        l=1
        result.append(words[0])
        while l<len(words):
            if checkAnagram(words[l-1],words[l]):
                l+=1
            else:
                result.append(words[l])
                l+=1
        return result
            