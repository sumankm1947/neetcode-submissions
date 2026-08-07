# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the linked list into 2 halves with slow and fast pointer
        p1 = head
        p2 = head
        isEven = False
        if head.next == None:
            return

        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next
        
        if p2.next != None and p2.next.next == None:
            p2 = p2.next
            isEven = True
        # print(p1.val)
        # print(p2.val)

        # reverse the second part of the string
        prev = p1.next
        if prev.next != None:
            curr = prev.next
            prev.next = None
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        
        p1 = head
        # now p1 is values at 0, 2, 4... indices 
        # now p2 is values at ...., 5, 3, 1 indices

        # now merge the 2 LL
        while p1.next != None and p2.next != None:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        
        # print(p1.val)
        # print(p1.next.val)
        # print(p2.val)
        if not isEven:
            temp = p1.next
            p1.next = p2
            p2.next = temp
            temp.next = None
            

