class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            narrowedPrefix = ""

            for i, char in enumerate(strs[i]):
                if char == prefix[i]:
                    narrowedPrefix += char
                    continue

                break

            if not narrowedPrefix:
                return ""

            prefix = narrowedPrefix

        return prefix



