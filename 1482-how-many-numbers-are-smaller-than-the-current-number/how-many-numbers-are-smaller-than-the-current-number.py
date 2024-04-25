class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = list(nums) 
        nums.sort()

        small = []
        count=0

        for i in range(len(arr)):
            count = 0
            for j in range(len(nums)):
                if arr[i] > nums[j]:
                    count += 1
            small.append(count)
        return small

        