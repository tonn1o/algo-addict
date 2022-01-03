# recursive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, leftIdx):
            if not nums:
                return -1 

            middleIdx = (len(nums) - 1) // 2
            middleValue = nums[middleIdx]
            
            if middleValue == target:
                return leftIdx + middleIdx
            
            if middleValue > target:
                return binarySearch(nums[:middleIdx], leftIdx)
            
            if middleValue < target:
                return binarySearch(nums[middleIdx + 1:], middleIdx + leftIdx + 1)
        
        return binarySearch(nums, 0)

# iterative 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            middleVal = nums[middle]
            
            if middleVal == target:
                return middle
            
            if target > middleVal:
                left = middle + 1
                
            if target < middleVal:
                right = middle - 1
                
        return - 1
        
    
