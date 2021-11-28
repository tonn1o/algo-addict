# Brute force

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0

        for i in range(n1):
            for j in range(n2):
                matchedLength = 0

                while matchedLength + i < n1 and j + matchedLength < n2 and nums1[i + matchedLength] == nums2[j + matchedLength]:
                    matchedLength += 1
                    ans = max(matchedLength, ans)

        return ans
