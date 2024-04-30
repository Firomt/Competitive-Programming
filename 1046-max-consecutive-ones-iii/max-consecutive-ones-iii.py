class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        has=[0]*2
        j=0
        i=0
        ans=0
        while(j<len(nums)):
            has[nums[j]]+=1
            if((j-i+1)-has[1]<=k):
                ans=max(j-i+1,ans)
            else:
                while((j-i+1)-has[1]>k):
                    has[nums[i]]-=1
                    i+=1
            j+=1
        return ans