class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1 
        
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            pivot = left + (right - left) // 2
            pivotVal = nums[pivot]
            
            if pivotVal > nums[pivot + 1]:
                right = pivot
            else:
                left = pivot + 1
            
        return left
