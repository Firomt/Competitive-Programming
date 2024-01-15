class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub=0
        prefix={0:1}
        cur_sum=0
        for i in nums:
            cur_sum+=i
            diff=cur_sum-k
            
            sub+= prefix.get(diff,0)
            prefix[cur_sum]=1 + prefix.get(cur_sum,0)
        return sub
            

                
                
        