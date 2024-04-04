class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)> len(s):
            return []
        pHash,sHash={},{}
        ans=[]
        for i in range(len(p)):
            pHash[p[i]]=1 + pHash.get(p[i],0)
            sHash[s[i]]=1 + sHash.get(s[i],0)
        
        if sHash==pHash:
            ans.append(0)

        l=0
        for r in range(len(p),len(s)):
            sHash[s[r]]= 1 + sHash.get(s[r],0)
            sHash[s[l]]-=1
            if sHash[s[l]]==0:
                sHash.pop(s[l])
            l+=1
            if sHash==pHash:
                ans.append(l)
        return ans


        