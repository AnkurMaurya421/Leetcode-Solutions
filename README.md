# Leetcode-Solutions
Repo to summarise all my leetcode submissions and approach.
This repository contains my solutions to LeetCode problems, organized by topic.  
Each problem includes a **link**, **difficulty**, and **approach summary**.
---
## Arrays
1. [Two Sum](https://leetcode.com/problems/two-sum/)
**Easy**
->Hashmap solution

2. [Concatenation of array](https://leetcode.com/problems/concatenation-of-array/) 
**Easy** 
->extend array to itself

3. [Container with most water](https://leetcode.com/problems/container-with-most-water/)
**Medium**
->Use greedy approach and two pointers to maximize the distance hence maximizing the area of less heighted pillar and moving to next pillar
4. [longest-subsequence-with-non-zero-bitwise-xor](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/)
**Medium**
->use the intuition that xor will be zero if all elements are zero
->if there are non zero elements and xor is still zero then we have to remove exactly on element to make it non zero
5. [best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Easy**
->set min and max to first element,set result to 0, iterate and update min and max to current element every time you found a new min...and also update the result with max-min every time you found the new min.
## Numbers
1. [Water Bottles](https://leetcode.com/problems/water-bottles/)
**Easy**
->Simple arithmetic division and multiplication to simulate the process
2. [Water Bottles 2](https://leetcode.com/problems/water-bottles-ii/)
**Medium**
->Just simulate the process on given conditions
3. [Compute Alternating Sum](https://leetcode.com/contest/weekly-contest-470/problems/compute-alternating-sum)
**Easy**
->simulate the process of alternating sum by using a boolean flag to track addition and subtraction
4. [earliest-time-to-finish-one-task](https://leetcode.com/problems/earliest-time-to-finish-one-task/)
**easy**
->Just calculate the time taken for each task and return the minimum time taken
## String
1. [reverseWords](https://leetcode.com/problems/reverse-words-in-a-string/)
**Medium**
-> simple stack approach
2. [majority-frequency-characters](https://leetcode.com/problems/majority-frequency-characters/)
**Easy**
->Simply store freq of each character then store freq as a key in another dictionary and characters as values..return the value of maximum lentgh and key.
3. [sum-of-elements-with-frequency-divisible-by-k](https://leetcode.com/contest/weekly-contest-471/problems/sum-of-elements-with-frequency-divisible-by-k/)
 **Easy**
-> Use a dictionary to count the frequency of each element in the array.
  Then, iterate through the dictionary and for each element whose frequency is divisible by k,
 add the product of the element and its frequency to the result.
4. [find-resultant-array-after-removing-anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)
**Easy**
-> create a funtion to check anagram and then iterate through the array
 using a pointer to check if the current word is an anagram of the previous word.
  If it is not an anagram, add it to the result array.

## Dynamic programming
1. [climbing-stairs](https://leetcode.com/problems/climbing-stairs/)
**Easy**
-> Use recursion with memoization to avoid recomputation of already solved subproblems. The number of ways to reach the nth step is the sum of the ways to reach the (n-1)th and (n-2)th steps.

