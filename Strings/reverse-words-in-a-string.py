# Problem: Water Bottles 2
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium
# Approach: 
#             1) Use a stack to store words
#             2) Reverse the stack
#             3) Join the words with a space in between




class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        s+=" "
        word=""
        for x in range(len(s)):
            if s[x]!=" ":
                word+=s[x]
            else:
                if word!="":
                    stack.append(word)
                    word=""
                else:
                    continue
        stack.reverse()
        result=" ".join(stack)
        return result

            