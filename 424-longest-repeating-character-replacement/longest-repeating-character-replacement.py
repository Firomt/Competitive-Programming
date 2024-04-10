class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count={}
        l, ans, max_freq=0, 0, 0
        for r in range(len(s)):
            char_count[s[r]]=1 + char_count.get(s[r],0)
            max_freq=max(max_freq,char_count[s[r]])
            
            while (r-l+1)-max_freq > k:
                char_count[s[l]]-=1
                l+=1
            ans=max(r-l+1,ans)
        return ans