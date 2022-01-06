class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        def find_rotate_idx():
            left = 0
            right = n - 2
            
            while left <= right:
                pivot = (left + right) // 2
                
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else: 
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else: 
                        left = pivot + 1
                
            return 0
                        
            
        def find_traget(left, right):
            while left <= right:
                pivot = (left + right) // 2
                k = nums[pivot]
                
                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] > target: 
                        right = pivot - 1
                    else:
                        left = pivot + 1
            
            return -1


        rotate_idx = find_rotate_idx()
        
        if nums[rotate_idx] == target:
            return rotate_idx
        
        if rotate_idx == 0:
            return find_traget(0, n - 1)

        if target < nums[0]:
            return find_traget(rotate_idx, n - 1)

        return find_traget(0, rotate_idx)


            
            
            
