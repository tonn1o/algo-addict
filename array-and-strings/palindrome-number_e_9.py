class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        n = len(xStr)

        for i in range(0, n // 2  + 1):
            if xStr[i] != xStr[n - 1 - i]:
                return False

        return True
