class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap={}
        maxLen=0
        i,j=0,0
        
        for j in range(len(s)):
            while s[j] in hashMap:
                del hashMap[s[i]]
                i+=1

            hashMap[s[j]]=1
            maxLen=max(maxLen, j-i+1)
            j+=1 

        return maxLen

