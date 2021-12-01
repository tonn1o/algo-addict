# O(n)
# can be solved without 2 pointers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        n = len(prices)

        maxDiff = 0
        minIdx = 0
        left = right = 0

        while right < n:
            diff = prices[right] - prices[left]

            maxDiff = max(diff, maxDiff)

            if prices[right] < prices[minIdx]:
                minIdx = right

            if left < right and left != minIdx:
                left = minIdx
                continue

            right += 1

        return maxDiff

