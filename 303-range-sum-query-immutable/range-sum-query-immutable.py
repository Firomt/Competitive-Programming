class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix_sum=[]
        prefix=0
        for num in nums:
            prefix+=num
            self.prefix_sum.append(prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right]-self.prefix_sum[left]+self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

    # def __init__(self, nums: List[int]):
    #     self.prefix_sum = [0]
    #     prefix = 0
    #     for num in nums:
    #         prefix += num
    #         self.prefix_sum.append(prefix)

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.prefix_sum[right + 1] - self.prefix_sum[left]


    