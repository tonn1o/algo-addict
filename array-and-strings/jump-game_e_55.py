class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return false

        n = len(nums)
        jumpsBuff = [True] * n

        def canFinish(idx):
            if not jumpsBuff[idx]:
                return False

            jumpSize = nums[idx]

            if idx + jumpSize >= n - 1:
                return True

            jumpRangeFrom = idx + 1
            jumpRangeTo = idx + jumpSize + 1

            if jumpRangeTo < n:
                for nextIdx in range(jumpRangeFrom, jumpRangeTo):
                    if canFinish(nextIdx):
                        return True

            jumpsBuff[idx] = False
            return False

        return canFinish(0)
