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
6. [longest-balanced-subarray-i](https://leetcode.com/problems/longest-balanced-subarray-i/)
**Medium**
-> Check all subarrays and count unique even and odd numbers using a set.Update the result if counts are equal.
7. [maximum-alternating-sum-of-squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)
**Medium**
-> convert each element to its square and then sort the array...half of the elements at negative positions should be the smallest
 for max alternating sum..so sum the smaller half as negative and larger half as positive and return the result

8. [minimum-operations-to-transform-array](https://leetcode.com/problems/minimum-operations-to-transform-array/)
**Medium**
->check if last element of nums2 can be achieved by minimum zero oepration...calculate the difference between corresponding elements of nums1 and nums2..sum the absolute differences
finally add minimum operations needed to achieve last element of nums2 from any element of nums1

9. [make-array-elements-equal-to-zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/description/)
**Easy**
-> if all elements are zero, each element can be removed in two ways (left or right), so return 2*n
              Calculate the total sum of the array
             Iterate through the array, maintaining left and right sums and checking conditions for valid removals
                #if leftsum == rightsum, the element can be removed from either side (2 ways)
                #if abs(leftsum - rightsum) == 1, the element can be removed from one side (1 way)

10. 
[the-two-sneaky-numbers-of-digitville](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)
**Easy**
-> use set to track seen numbers, if a number is seen again, it's one of the sneaky numbers
11. [minimum-time-to-make-rope-colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) **Medium**
-> greedy approach, iterate through the rope and whenever two adjacent colors are the same, remove the one with the smaller cost






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
5. [smallest-missing-multiple-of-k](https://leetcode.com/problems/smallest-missing-multiple-of-k/)
**Easy**
->Generate multiples of k and check which is the smallest not present in the array.
6. [ maximize-sum-of-squares-of-digits]
( https://leetcode.com/problems/maximize-sum-of-squares-of-digits/)
**Medium**
-> calculate how many 9's can fit in the sum and check for remainder..if remainder exists we need one more digit.check if total digits needed is less than or equal to num..if yes construct the number with 9's , remainder and 0's else return empty string
7.[smallest-number-with-all-set-bits](https://leetcode.com/problems/smallest-number-with-all-set-bits/)
**Easy**
-> set bit numbers are of form (2 ** n)-1 . So we can keep on checking for (2**n)-1 until we find the number greater than or equal to num.






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
5. [final-value-of-variable-after-performing-operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/)
**Easy**
->Approach:set x=0 and perform the operation on given condition
6. [check-if-digits-are-equal-in-string-after-operations-i](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i)
**Easy**
->create a funtion for the given operation so that we can repeatedly call it until the length of string is 2. finally check if both digits are equal or not.
7. [lexicographically-smallest-string-after-reverse]
(https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/)
**Medium**
->check all possible reversals by iterating through each index and reversing the substring from start to that index and from that index to end..keep track of smallest string and return it
8. [remove-zeros-in-decimal-representation]
(https://leetcode.com/problems/remove-zeros-in-decimal-representation/)
**Easy**
->Approach: convert number to string and iterate through each character..add non zero characters to result string..finally convert result string to integer and return
9. [Number of Laser Beams in a Bank]
( https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)
**Medium**
->basically number of beams between two subsequent rows containing device will be product of sum of devices of each row





## Dynamic programming
1. [climbing-stairs](https://leetcode.com/problems/climbing-stairs/)
**Easy**
-> Use recursion with memoization to avoid recomputation of already solved subproblems. The number of ways to reach the nth step is the sum of the ways to reach the (n-1)th and (n-2)th steps.





## Linked List
1. [middle-of-the-linked-list](https://leetcode.com/problems/middle-of-the-linked-list/)
**Easy**
-> get to the middle by initializing two pointers at ste start and moving one by one step and another by two step when the two step pointer reaches the end one step pointer will be at the middle of linked list.
2. [reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)**Easy**
->Iterate through the linked list and rebuild the links in reverse order by keeping track of the next node.
3. [delete-node-in-a-linked-list](https://leetcode.com/problems/delete-node-in-a-linked-list/)
**Medium**
->copy the value of next node to current node and move to next node until we reach the end of linked list
4.[merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists/)
**Easy**
->recursively iterate through both linked list always choosing the smaller node and linking it to the next bigger node. return the choosen node.
5. [remove-nth-node-from-end-of-list] **Medium** 
->move a dummy pointer n time forward ..then start moving another pointer with that dummy pointer
if dummy pointer reached at last node that means another pointer is at nth node..then remove nth node
6. [delete-nodes-from-linked-list-present-in-array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)
**Medium**
->use a set to store the values in the array for O(1) lookup, then iterate through the linked list and remove nodes whose values are in the set






# Binary search
1. [sqrtx](https://leetcode.com/problems/sqrtx/)
 **Easy**
-> Binary search between 0 to x to find the integer square root. If mid*mid is equal to x, return mid. If mid*mid is greater than x, move the right pointer to mid-1. If mid*mid is less than x, update maxi to mid if mid is greater than maxi and move the left pointer to mid+1. Finally, return maxi.
