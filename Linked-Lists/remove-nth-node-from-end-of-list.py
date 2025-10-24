


# Problem: remove-nth-node-from-end-of-list
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Approach: move a dummy pointer n time forward ..then start moving another pointer with that dummy pointer
#if dummy pointer reached at last node that means another pointer is at nth node..then remove nth node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        #initialize a pointer from start and move that to n steps
        pointer=head
        for _ in range (n):
            pointer=pointer.next
        

        #check if pointer is already at end null node..that means we have to remove head only
        if not pointer:
            return head.next
        # if pointer is at the valid end node that means we have to remove 2nd node
        if not pointer.next:
            head.next=head.next.next
            return head
        
        #initialize pointer2 and move both pointers by one step untill pointer hits the end node
        #that's when we know pointer2 will be at nth node
        #then remove nth node by modyfying connections
        #initialize prev as None and store the node as you move on to next node
        pointer2=head
        #prev=None
        while pointer.next:
            #prev=pointer2
            pointer2=pointer2.next
            pointer=pointer.next
       
        pointer2.next=pointer2.next.next
        return head