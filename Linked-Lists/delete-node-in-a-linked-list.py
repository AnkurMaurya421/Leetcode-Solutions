


# Problem: delete-node-in-a-linked-list
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Difficulty: Medium
# Approach: copy the value of next node to current node and move to next node until we reach the end of linked list





class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        while node.next:
            prev=node
            node.val=node.next.val
            node=node.next
        prev.next=None