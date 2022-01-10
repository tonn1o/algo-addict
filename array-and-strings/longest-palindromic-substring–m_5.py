class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return s
        
        res = s[0]
        n = len(s)
        
        def getPalindromicSubstr(idx):
            firstSub = ''
            secondSub = ''
            
            if idx > 0 and s[idx - 1] == s[idx + 1]:
                left = idx - 1
                right = idx + 1
                firstSub = s[idx]
                
                while left >= 0 and right <= n - 1 and s[left] == s[right]:
                    firstSub = s[left] + firstSub + s[right]
                    left -= 1
                    right += 1
                    
            
            if s[idx] == s[idx + 1]:
                left = idx
                right = idx + 1
                
                while left >= 0 and right <= n - 1 and s[left] == s[right]:
                    secondSub = s[left] + secondSub + s[right]
                    left -= 1
                    right += 1
                    
            return firstSub if len(firstSub) > len (secondSub) else secondSub
                    
                
        
        for idx in range(n - 1):
            substr = getPalindromicSubstr(idx)
            res = substr if len(substr) > len(res) else res
            
        return res
            
            
