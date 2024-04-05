class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt, cur_cnt, ans, l=0, 0, 0, 0
        for  r in range(len(nums)):
            if nums[r]%2 != 0:
                cur_cnt +=1
                cnt=0
            if cur_cnt == k:
                while l < len(nums) and nums[l]%2==0:
                    cnt+=1
                    l+=1
                cnt+=1
                cur_cnt-=1
                l+=1
            ans+=cnt
        return ans

        
     
            
