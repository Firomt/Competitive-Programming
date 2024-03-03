class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True

        seq=0
        for i in range(len(t)):
            if t[i]==s[seq]:
                seq+=1
            if seq==len(s):
                return True
        return False

        


    

        