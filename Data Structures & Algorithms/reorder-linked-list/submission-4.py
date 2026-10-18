# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        prev = slow.next = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        head2 = prev

        while head2:
            temp1, temp2 = head.next, head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2






