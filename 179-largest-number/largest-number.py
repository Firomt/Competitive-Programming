class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=[]
        for num in nums:
            ans.append(str(num))
        for i in range(len(ans)):
            for j in range(i+1, len(ans)):
                if (ans[i] + ans[j]) >= (ans[j]+ans[i]):
                    continue
                else:
                    ans[i], ans[j]=ans[j], ans[i]

        if int(''.join(ans))==0:
            return '0'
        
        return ''.join(ans)
        



    
        
