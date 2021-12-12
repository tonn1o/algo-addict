class Solution:
    def romanToInt(self, s: str) -> int:
        
        if not s: return 0
        
        rMap = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        
        n = len(s)
        sum = 0
        i = 0
        
        while i < n:
            num = s[i:i+2]
            
            if num in rMap:
                sum += rMap[num]
                i += 2
            else:
                sum += rMap[s[i]]
                i += 1
                
        return sum
                
        
