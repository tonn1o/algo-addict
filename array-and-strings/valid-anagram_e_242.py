class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = collections.defaultdict(int)
        
        for c in s:
            charCount[c] += 1
            
        for c in t:
            if charCount[c] == 0: 
                return False
            
            charCount[c] -= 1
        
        return True
        
