class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)//2):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
        