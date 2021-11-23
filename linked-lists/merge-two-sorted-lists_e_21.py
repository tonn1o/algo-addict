# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode()
        tail = dummy

        headFirst = l1
        headSecond = l2

        while headFirst or headSecond:
            if headFirst and headSecond:
                if headFirst.val < headSecond.val:
                    tail.next = ListNode(headFirst.val)
                    tail = tail.next
                    headFirst = headFirst.next
                else:
                    tail.next = ListNode(headSecond.val)
                    tail = tail.next
                    headSecond = headSecond.next
            elif not headFirst:
                tail.next = ListNode(headSecond.val)
                tail = tail.next
                headSecond = headSecond.next
            else:
                tail.next = ListNode(headFirst.val)
                tail = tail.next
                headFirst = headFirst.next

        return dummy.next




