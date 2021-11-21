# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        node = head
        listLen = 0
        
        while node != None:
            node = node.next
            listLen += 1
            
        node = head
        prev = None
        i = 0
        expectedIdx = listLen - n
        
        while i <= expectedIdx:
            if i == expectedIdx:
                if prev:
                    prev.next = node.next    
                else:
                    return node.next
                
                break

            prev = node
            node = node.next
            i += 1
            
        return head
