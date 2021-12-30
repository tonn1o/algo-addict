# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        visitedDict = dict()
        
        def hasCycle(node):
            if not node: 
                return False
            
            if node in visitedDict and visitedDict[node]: 
                return True
            
            visitedDict[node] = True
            
            return hasCycle(node.next)
        
        return hasCycle(head)
    

# Alt
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        visitedDict = dict()
        
        node = head
        
        while node:
            if node in visitedDict:
                return True

            visitedDict[node] = True
            
            node = node.next
            
        return False
