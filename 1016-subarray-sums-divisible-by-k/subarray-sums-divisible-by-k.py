class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_subarray=0
        cur_sum=0
        remainders={0:1}

        for i in nums:
            cur_sum+=i
            remainder=cur_sum % k
            if remainder in remainders:
                count_subarray += remainders[remainder]
            remainders[remainder] = 1 + remainders.get(remainder,0)

        return count_subarray
        