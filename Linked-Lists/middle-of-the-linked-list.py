

# Problem: middle-of-the-linked-list
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Approach: get to the middle by initializing two pointers at ste start and moving one by one step and another by two step when the two step
#            pointer reaches the end one step pointer will be at the middle of linked list.





# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oneStepNode=head    #initialize two pointer at the start and move one pointer by one step and 
        twoStepNode=head    #other pointer by two step ..if two step pointer can move further that means one step pointer is in middle of linked list
        while twoStepNode.next: #if two step pointer is at the end , return one step pointer 
            oneStepNode=oneStepNode.next      # move both pointer 
            twoStepNode=twoStepNode.next.next
            if not twoStepNode: #there is a chance that two step pointer becomes Null..then while condition will throw error..in this case return one step pointer
                return oneStepNode
        return oneStepNode # if while condition fails that means two step pointer is at last node then return one step pointer