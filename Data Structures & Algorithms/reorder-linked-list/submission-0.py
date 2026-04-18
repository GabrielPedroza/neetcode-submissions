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
        
        node = prev
        
        while node:
            temp1, temp2 = head.next, node.next

            head.next = node
            node.next = temp1

            head = temp1
            node = temp2