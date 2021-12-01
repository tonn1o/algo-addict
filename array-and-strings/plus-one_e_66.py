class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = []
        reminder = 1

        for i in range(n - 1, -1, -1):
            r = digits[i] + reminder

            if (r == 10):
                ans.insert(0, 0)
                reminder = 1
            else:
                ans.insert(0, r)
                reminder = 0

        if reminder == 1:
            ans.insert(0, 1)

        return ans
