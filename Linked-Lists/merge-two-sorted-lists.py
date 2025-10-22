


# Problem: merge-two-sorted-lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Approach: recursively iterate through both linked list always choosing the smaller node and linking it to the next bigger node. return the choosen node.
# Time Complexity: O(n+m) where n and m are the lengths of the two linked lists.






from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recur (l1,l2):
            if not l1 and not l2:
                return None
            if l1 and not l2:
                return l1
            if l2 and not l1:
                return l2
            if l1.val>l2.val:
                l1,l2=l2,l1
            l1.next=recur(l1.next,l2)
            return l1
        return recur(list1,list2)
