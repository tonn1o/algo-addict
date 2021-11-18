# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getNumFromReversedLinkedList(l1)
        num2 = self.getNumFromReversedLinkedList(l2)
        sum = str(num1 + num2)

        cur = dummy = ListNode()

        for s in reversed(sum):
            cur.next = ListNode(s)
            cur = cur.next

        return dummy.next



    def getNumFromReversedLinkedList(self, list: Optional[ListNode]):
        tail = list
        num = []

        while tail:
            num.insert(0, str(tail.val))
            tail = tail.next

        return int(''.join(num))

