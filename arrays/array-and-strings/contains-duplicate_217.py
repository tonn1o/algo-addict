class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existingValuesObj = {}

        for num in nums:
            if num in existingValuesObj:
                return True

            existingValuesObj[num] = True

        return False
