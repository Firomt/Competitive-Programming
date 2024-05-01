class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = count = 0
        for i in range(k):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                count += 1
        ans = max(ans, count)
        
        for i in range(k, len(s)):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                count += 1
            if s[i - k] in {'a', 'e', 'i', 'o', 'u'}:
                count -= 1
            ans = max(ans, count)
        
        return ans
        