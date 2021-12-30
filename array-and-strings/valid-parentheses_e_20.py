class Solution:
    def isValid(self, s: str) -> bool:
        open = set(['(', '{', '['])
        
        if not s or len(s) % 2 or not s[0] in open:
            return False
        
        expectedCloseChars = []
        
        for char in s:
            if char in open:        
                closeChar = None 
                
                if char == '(':
                    closeChar = ')'
                    
                if char == '{':
                    closeChar = '}'
                    
                if char == '[':
                    closeChar = ']'
                    
                expectedCloseChars.append(closeChar)
            else:
                if not expectedCloseChars:
                    return False
                
                closeChar = expectedCloseChars.pop()
                
                if char != closeChar:
                    return False
        
        return len(expectedCloseChars) == 0
