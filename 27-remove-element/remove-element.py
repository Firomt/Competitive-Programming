class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=len(nums)-1
        while val in nums:
            if nums[i]==val:
                nums.remove(nums[i])
                i-=1
            else:
                i-=1
        return len(nums)
        