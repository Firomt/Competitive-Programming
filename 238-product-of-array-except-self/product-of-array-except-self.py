class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        total_pro=1
        count=nums.count(0)
        for num in nums:
            total_pro *= num

        for num in nums:
            if num != 0:
                ans.append(int(total_pro/num))
            else:
                j=0
                current_pro=1
                # if count > 1:
                #     ans.append(int(0))
                # else:
                while nums[j] != num:
                    current_pro *= nums[j]
                    j+=1
                j=j+1
                while j < len(nums):
                    current_pro *= nums[j]
                    j+=1
                ans.append(int(current_pro))
        return ans
        

    