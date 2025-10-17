


# Problem: reverse-linked-list
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Approach: Iterate through the linked list and rebuild the links in reverse order by keeping track of the next node.







# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head!=None: 
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev