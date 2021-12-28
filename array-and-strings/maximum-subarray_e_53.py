class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]
        sum = 0 

        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
                
            res = max(res, sum)
            
        return res
