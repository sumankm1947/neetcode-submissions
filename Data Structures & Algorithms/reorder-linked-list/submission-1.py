# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the linked list into 2 halves with slow and fast pointer
        slow = head
        fast = head
        if head.next == None:
            return

        # split
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # join
        first = head
        second = prev
        while first and second:
            ft = first.next
            st = second.next
            first.next = second
            second.next = ft
            first = ft
            second = st


