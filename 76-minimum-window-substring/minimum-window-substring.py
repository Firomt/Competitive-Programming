class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        cnt_T=Counter(t)
        window={}
        have,need=0,len(cnt_T)
        ans,ansLen=[-1,-1], float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1 + window.get(c,0)

            if c in cnt_T and window[c]==cnt_T[c]:
                have+=1
            while have==need:
                if ( r-l+1)  < ansLen:
                    ans=[l,r]
                    ansLen=r-l+1

                window[s[l]]-=1
                if s[l] in cnt_T and window[s[l]]<cnt_T[s[l]]:
                    have-=1
                l+=1
        l,r=ans
        return s[l:r+1] if ansLen != float("infinity") else ""
                


