class Solution:
    def sortSentence(self, s: str) -> str:
        ls=list(s.split())
        ans=[0]*len(ls)
        for word in ls:
            ind= int(word[-1])
            ans[ind-1]=word[:-1]
        
        return ' '.join(ans)