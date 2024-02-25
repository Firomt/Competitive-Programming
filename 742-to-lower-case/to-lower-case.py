class Solution:
    def toLowerCase(self, s: str) -> str:
        l=list(s)
        for i in range(len(l)):
            if l[i].isupper():
                l[i]=l[i].lower()

        
        return ''.join(l)
     
        