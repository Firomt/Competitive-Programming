class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=0
        minimum=prefix
        for i in range(len(nums)):
            prefix += nums[i]
            minimum=min(minimum,prefix)

        if minimum < 0:
            return abs(minimum)+1
        else:
            return 1


        