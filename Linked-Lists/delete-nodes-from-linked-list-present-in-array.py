

# Problem: delete-nodes-from-linked-list-present-in-array
# Link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Difficulty: Medium
# Approach: use a set to store the values in the array for O(1) lookup, then iterate through the linked list and remove nodes whose values are in the set


from typing import List, Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        result=None
        bucket=set(nums)
        while head:
            if head.val in bucket:
                if prev:
                    prev.next=head.next
            else:
                if prev:
                    prev=head
                else:
                    prev=head
                    result=head
            head=head.next
        return result