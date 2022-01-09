        left = 0
        right = len(nums) - 2

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            elif nums[left] > nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return nums[0]
