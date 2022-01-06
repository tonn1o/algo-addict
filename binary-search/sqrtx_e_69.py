class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            pivotSquare = pivot * pivot
            
            if pivotSquare == x:
                return pivot
            elif pivotSquare < x:
                left = pivot + 1
            else: 
                right = pivot - 1
                
        return right
