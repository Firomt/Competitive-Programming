class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_subarray=0
        cur_sum=0
        prefix_hash=collections.defaultdict(int)
        prefix_hash[0]=1

        for i in nums:
            cur_sum+=i
            if cur_sum % k in prefix_hash:
                count_subarray += prefix_hash[cur_sum % k]
            prefix_hash[cur_sum % k] += 1

        return count_subarray
        