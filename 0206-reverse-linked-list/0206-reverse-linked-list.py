# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # 1. Save the rest of the list
            curr.next = prev # 2. Reverse the link
            prev = curr      # 3. Move prev one step forward
            curr = nxt       # 4. Move curr one step forward
            
        # By the end, prev will be standing on the new head of the reversed list
        return prev