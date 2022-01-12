# ETL O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            sum = 0

            for j in range(i, n):
                sum += nums[j]

                if sum == k:
                    res += 1

        return res

# O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = collections.defaultdict(int)
        res = sum = 0
        sums[0] = 1

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                res += 1

            if sum

        return res
