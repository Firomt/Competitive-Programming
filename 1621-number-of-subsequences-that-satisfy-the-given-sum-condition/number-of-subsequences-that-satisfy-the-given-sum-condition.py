class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result, modulo = 0, 10**9 + 7

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                result += pow(2, right - left, modulo)
                left += 1

        return result % modulo
        