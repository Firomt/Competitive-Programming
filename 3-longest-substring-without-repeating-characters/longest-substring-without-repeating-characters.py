class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap={}
        maxLen=1
        i,j=0,0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        while i<= j and j in range(len(s)):
            if s[j] in hashMap:
                while s[j] in hashMap:
                    del hashMap[s[i]]
                    i+=1

            hashMap[s[j]]=1
            maxLen=max(maxLen, j-i+1)
            j+=1 

        return maxLen

