class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word in s.split() if word]
        return len(words[-1])
        