class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        substrings = []
        longest = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(s[i:j]) > 1:
                    substrings.append(s[i:j])
                    
        for sub in substrings:
            is_nice = True
            for c in sub:
                if c.islower():
                    upper_c = c.upper()
                    if upper_c not in sub:
                        is_nice = False
                        break
                elif c.isupper():
                    lower_c = c.lower()
                    if lower_c not in sub:
                        is_nice = False
                        break
            
            if is_nice and len(sub) > len(longest):
                longest = sub
        
        return longest
        