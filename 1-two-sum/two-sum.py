class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={}
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference in checked:
                return [checked[difference],i]
            else:
                checked[nums[i]]=i

            


        
        