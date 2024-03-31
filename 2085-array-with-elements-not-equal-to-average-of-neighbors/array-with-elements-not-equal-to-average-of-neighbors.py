class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        for i in range(1, n - 1):
            if (nums[i - 1] < nums[i] < nums[i + 1]) or (nums[i - 1] > nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums

        