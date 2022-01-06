# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 0, n
        
        if n < 2:
            return n
        
        while left <= right:
            pivot = (right + left) // 2
            isBad = isBadVersion(pivot)
            
            if isBad and not isBadVersion(pivot - 1):
                return pivot
            elif isBad:
                right = pivot - 1
            else: 
                left = pivot + 1
                
