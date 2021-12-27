class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        left = [None] * n
        right = [None] * n
        
        right[n - 1] = left[0] = 1
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            
        for i in range(n):
            res.append(left[i] * right[i])
            
        return res
