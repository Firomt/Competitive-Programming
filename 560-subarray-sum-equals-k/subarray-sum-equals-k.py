class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt_subarray=0
        prefix_freq={0:1}
        cur_sum=0
        for num in nums:
            cur_sum+=num
            diff=cur_sum-k
            cnt_subarray+=prefix_freq.get(diff,0)
            prefix_freq[cur_sum]= 1 + prefix_freq.get(cur_sum, 0)
        return cnt_subarray


                
                
        