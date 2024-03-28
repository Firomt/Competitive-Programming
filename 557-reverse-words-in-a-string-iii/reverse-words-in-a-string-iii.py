class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split())
        reverse=[]
        for i in range(len(s)):
            rev=list(s[i])
            reverse.append(''.join(rev[::-1]))
        return ' '.join(reverse)

            

        